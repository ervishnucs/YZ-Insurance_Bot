import React, { useState, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [conversation, setConversation] = useState([]);
  const sessionId = "session1"; // Static session ID for now
  const [isRecording, setIsRecording] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunks = useRef([]); // Store audio chunks

  // Handle sending the question to the chatbot API
  const handleSend = async (query) => {
    if (query.trim()) {
      setIsLoading(true);

      try {
        const res = await axios.post("http://localhost:8000/ask", {
          question: query,
          session_id: sessionId,
        });

        const botResponse = res.data.response;
        setConversation((prevConversation) => [
          ...prevConversation,
          { question: query, botResponse },
        ]);
        setQuestion(""); // Clear input after sending
      } catch (error) {
        console.error("Error fetching response:", error);
      }

      setIsLoading(false);
    }
  };

  // Play audio using browser's TTS
  const handlePlayAudio = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);
  };

  // Start recording audio
  const startRecording = () => {
    setIsRecording(true);
    audioChunks.current = [];

    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        mediaRecorderRef.current = new MediaRecorder(stream);
        mediaRecorderRef.current.ondataavailable = (event) => {
          audioChunks.current.push(event.data);
        };

        // Stop recording handler
        mediaRecorderRef.current.onstop = async () => {
          const audioBlob = new Blob(audioChunks.current, {
            type: "audio/wav",
          });

          // Example: Simulate a transcription result
          const transcript = "What are the premium rates?";
          setQuestion(transcript); // Set transcript as the question
          await handleSend(transcript); // Automatically send the question
        };

        mediaRecorderRef.current.start();
      })
      .catch((error) => {
        console.error("Error accessing microphone:", error);
      });
  };

  // Stop recording audio
  const stopRecording = () => {
    setIsRecording(false);
    mediaRecorderRef.current?.stop(); // Stop recording and trigger `onstop`
  };

  return (
    <div className="chatbot-container">
      <h1>CHATBOT</h1>
      <div className="chat-window">
        {conversation.map((msg, index) => (
          <div key={index} className="message-container">
            <div className="chat-message user-message">
              <p>
                <strong>User:</strong> {msg.question}
              </p>
            </div>
            <div className="chat-message bot-message">
              <p>
                <strong>Bot:</strong> {msg.botResponse}
              </p>
              <button
                className="audio-btn"
                onClick={() => handlePlayAudio(msg.botResponse)}
              >
                🔊
              </button>
            </div>
          </div>
        ))}
      </div>
      <div className="input-container bottom">
        <input
          type="text"
          value={isRecording ? "Listening..." : question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me something..."
          disabled={isLoading || isRecording}
        />
        <button
          className="btn"
          onClick={() => handleSend(question)}
          disabled={isLoading}
        >
          {isLoading ? "Loading..." : "Send"}
        </button>
        <button
          className="btn1"
          onClick={isRecording ? stopRecording : startRecording}
        >
          {isRecording ? "Stop Recording" : "🎤 Record"}
        </button>
        {isLoading && <div className="loading-spinner"></div>}
      </div>
    </div>
  );
}

export default App;
