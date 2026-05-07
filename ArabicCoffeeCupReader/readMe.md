🔮 Overview
The Digital Tasseographer is an AI-powered Lebanese Coffee Reader. Using a state-of-the-art LangGraph workflow and Gemini 2.5/3.1 vision models, the application analyzes three distinct views of a coffee cup (Right, Left, and Down) to provide a mystical, culturally-attuned reading focusing on Arabic symbolism, family, and social life.

🏗️ Technical Architecture
This project utilizes a multi-agent orchestration pattern to ensure high-quality readings:

Cleaner Node: Pre-processes base64 images and prepares the multimodal payload.

Generation Node: Uses Gemini 2.5 Flash to interpret symbols and generate the "Fortune."

Critique Node: A self-correction step that verifies the reading's consistency against the visual data before final output.

🛠️ Tech Stack
Orchestration: LangGraph (StateGraph)

LLM: Google Gemini 2.5/3.1 (Multimodal Vision)

Frontend: Streamlit

🚀 Getting Started
1. Prerequisites
You will need the following API keys stored in your Google Colab Secrets (🔑):

GEMINI_API_KEY: Obtain from Google AI Studio.

NGROK_AUTH: Obtain from Ngrok Dashboard.

2. Installation
Bash
pip install langchain-google-genai langgraph streamlit pyngrok
3. Running the App
Open the project in Google Colab.

Run the Launch Cell to map environment variables and start the Streamlit server.

Click the generated Ngrok URL to access your coffee reader.

📸 How It Works
Upload Images: Take three photos of your finished coffee cup.

Analyze: The images are passed through the graph.

Reveal: The AI identifies patterns (like snakes, birds, or eyes) and generates a stylized reading in a dedicated "mystical" UI.
Deployment: Google Colab with pyngrok for tunneling

State Management: MemorySaver for persistent session threads
