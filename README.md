# Insurance Chatbot with Conversational RAG and VectorDB

## Problem
Insurance agents have to provide instant, accurate responses to customer queries, but accessing relevant information quickly can be challenging.

## Solution
The conversational RAG Bot with voice-enabled interaction addresses this by providing seamless, real-time assistance integrated into the frontend.

## Tools
- **LLM - Cohere’s Command-r-plus**: Best suited for complex RAG workflows with long context.
- **VectorDB - Qdrant Vector Store & ChromaDB**: Useful for semantic-based matching.
- **Document Loader**: Unstructured text extraction.
- **Uvicorn**: ASGI web server.
- **FastAPI**: High-performance web framework for APIs.
- **Axios**: HTTP client for API requests.
- **Browser API**:
  - SpeechRecognition - Voice to Text conversion
  - SpeechSynthesis - Text to Speech conversion

## Implementations
- Loaded 20+ Policy documents
- **Conversational RAG Technique**
  - Indexing
  - Retrieval (Chat History + Present user Query)
  - Generation
- **Speech Recognition**
  - Recognize voice input from users and convert it into text in real-time.
  - Enabling the chatbot to respond with audio output.

## Project Outcome
Created a responsive, real-time chatbot with retrieval-based knowledge augmentation to answer user queries related to policy documents.

## Chatbot Interface
![Chatbot Interface](https://drive.google.com/uc?id=1j3EKyW6G_fASN7B-4xdbtQ5K58dXYoID)
