🧘 Mental Wellness Partner: State-Aware AI Therapist
Mental Wellness Partner is a sophisticated AI-driven therapeutic assistant that utilizes a structured, session-aware architecture to conduct multi-stage mental health support.

Unlike generic chatbots, this system distinguishes between Intake (Discovery) and Follow-up (Treatment) sessions. It maintains a persistent clinical record using JSON-based state management, allowing the AI to lead conversations based on historical context, defined care paths, and evolving patient needs.

🧠 Core Engineering Principles
1. Dynamic Session Management
The application identifies the session stage by querying the persistent clinical record:

Intake Phase (Session 1): The AI utilizes a "Discovery Mode," focusing on open-ended questions, background gathering, and rapport building.

Follow-up Phase (Session 2+): The AI shifts to "Treatment Mode," referencing past session summaries and established care paths to provide continuity.

2. Autonomous Conversational Leads
The model doesn't just wait for user input. It proactively generates "Session Openers" tailored to the patient's history, ensuring the therapy session has a clear direction from the moment it begins.

3. Automated Clinical Summarization
At the end of each session, a dedicated summarization node processes the entire dialogue history to generate a professional clinical note. This "compresses" the memory to keep the context window efficient while preserving critical diagnostic details.

🛠️ Tech Stack
LLM: Google Gemini 2.0 Flash (Optimized for low-latency, empathetic dialogue).

Framework: Streamlit (Front-end chat interface).

Orchestration: Custom State-Logic (Node-based sequence).

Persistence: Structured JSON serialization (facilitating "Zero-Footprint" database deployment).

Deployment: Ngrok Tunneling (enabling secure, mobile-accessible sessions).

📋 Features
Persistent Patient Records: Sidebar integration shows historical session notes, allowing users to see the AI's "memory" in real-time.

Context-Aware Logic: Uses os.environ to securely manage API keys and session states.

Resilience Engineering: Built-in exponential backoff to handle 503 "High Demand" errors from AI backends.

Mobile-Ready Interface: Fully responsive design accessible via secure tunnel.

🚀 Installation & Usage
Dependencies:

Bash
pip install streamlit langchain-google-genai pyngrok
Environment Setup:

Add your GEMINI_API_KEY and NGROK_AUTH to your environment variables or Google Colab Secrets.

Run Application:

Bash
streamlit run therapist_app.py
