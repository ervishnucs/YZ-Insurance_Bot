<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #003366;
        }
        .section {
            margin-bottom: 20px;
            padding: 10px;
            border-left: 5px solid #003366;
            background: #e6f2ff;
        }
        .image-container {
            text-align: center;
            margin-top: 20px;
        }
        img {
            width: 80%;
            max-width: 600px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Insurance Chatbot with Conversational RAG and VectorDB</h1>
        <p><strong>Problem:</strong> Insurance agents have to provide instant, accurate responses to customer queries, but accessing relevant information quickly can be challenging.</p>
        
        <div class="section">
            <p><strong>Solution:</strong> The conversational RAG Bot with voice-enabled interaction addresses this by providing seamless, real-time assistance integrated into the frontend.</p>
        </div>
        
        <div class="section">
            <h2>Tools</h2>
            <ul>
                <li><strong>LLM - Cohere’s Command-r-plus:</strong> Best suited for complex RAG workflows with long context.</li>
                <li><strong>VectorDB - Qdrant Vector Store:</strong> Useful for semantic-based matching.</li>
                <li><strong>Document Loader:</strong> Unstructured text extraction.</li>
                <li><strong>Uvicorn:</strong> ASGI web server.</li>
                <li><strong>FastAPI:</strong> High-performance web framework for APIs.</li>
                <li><strong>Axios:</strong> HTTP client for API requests.</li>
                <li><strong>Browser API:</strong>
                    <ul>
                        <li>SpeechRecognition - Voice to Text conversion</li>
                        <li>SpeechSynthesis - Text to Speech conversion</li>
                    </ul>
                </li>
            </ul>
        </div>
        
        <div class="section">
            <h2>Implementations</h2>
            <ul>
                <li>Loaded 20+ Policy documents</li>
                <li><strong>Conversational RAG Technique</strong>
                    <ul>
                        <li>Indexing</li>
                        <li>Retrieval (Chat History + Present user Query)</li>
                        <li>Generation</li>
                    </ul>
                </li>
                <li><strong>Speech Recognition</strong>
                    <ul>
                        <li>Recognize voice input from users and convert it into text in real-time.</li>
                        <li>Enabling the chatbot to respond with audio output.</li>
                    </ul>
                </li>
            </ul>
        </div>
        
        <div class="section">
            <h2>Project Outcome</h2>
            <p>Created a responsive, real-time chatbot with retrieval-based knowledge augmentation to answer user queries related to policy documents.</p>
        </div>
        
        <div class="image-container">
            <img src="https://drive.google.com/file/d/1j3EKyW6G_fASN7B-4xdbtQ5K58dXYoID/view?usp=sharing" alt="Chatbot Interface">
        </div>
    </div>
</body>
</html>
