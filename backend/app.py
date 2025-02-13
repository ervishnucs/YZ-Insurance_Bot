import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_cohere import ChatCohere
from fastapi.responses import JSONResponse

# Initialize FastAPI app
app = FastAPI()


# Allow CORS from any origin (for development purposes only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

# Load environment variables
os.environ["COHERE_API_KEY"] = "key"

# Initialize LLM and embeddings
llm = ChatCohere(model="command-r-plus")
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
loader = PyPDFLoader(r"policies")

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vector_store = Chroma.from_documents(documents=splits, embedding=embeddings_model)

retriever = vector_store.as_retriever(search_type="mmr")

# Create prompts
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question, "
    "reformulate it if needed and answer the question concisely."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        ("human", "{input}"),
    ]
)

system_prompt = (
      "You are Ai Assistant help user to understand the document by answering the questions of the user "
      "Avoid Haullicinating answer from the {context}"

   "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# Create chains
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# Store chat history
store = {}

class QuestionRequest(BaseModel):
    question: str
    session_id: str

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Define the conversational RAG chain
conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)
import logging

# Add logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Define the FastAPI route
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        # Invoke the chain with session history and question
        session_history = get_session_history(request.session_id).messages
        response = conversational_rag_chain.invoke(
            {"input": request.question, "chat_history": session_history},
            {"configurable": {"session_id": request.session_id}}
        )
        if "answer" in response:
                 return JSONResponse(content={"response": response["answer"]})
        else:
                raise HTTPException(status_code=500, detail="Failed to retrieve an answer from the chain")

    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
