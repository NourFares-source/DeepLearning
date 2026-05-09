🩸 Overview
MediScan AI is a secure, privacy-first medical report analyzer. It allows users to upload blood test results (PDF or Image) and receive personalized health insights based on their specific concerns (e.g., "Energy & Fatigue" or "Heart Health").

The project leverages a Self-Correction Graph to ensure high clinical accuracy and utilizes Microsoft Presidio to ensure no personal data ever leaves the local environment.

🏗️ The "Double-Doctor" Architecture
This application uses a sophisticated LangGraph workflow:

The Collector: Extracts text from PDFs (pdfplumber) or Images (Gemini Vision).

The PII Scrubber (Security Node): Uses Microsoft Presidio to identify and redact Names, Phones, and Emails before the data is sent to the LLM.

The Analyst: A Gemini-powered agent that interprets results based on the user's intent.

The Auditor (Self-Correction): A second "doctor" node that verifies the analysis against the original data. If a mistake is found, it sends the report back for a rewrite.

🛠️ Tech Stack
Orchestration: LangGraph (Stateful Multi-Agent system)

Privacy: Microsoft Presidio (NLP-based Anonymization)

LLMs: Google Gemini 2.5/1.5 Pro (Multimodal)

Parsing: pdfplumber & PIL

Frontend: Streamlit

🛡️ Privacy & Compliance
Security was the #1 priority for this project:

Zero-Knowledge Analysis: The AI model only sees "redacted" text (e.g., [REDACTED_NAME]).

Hallucination Guard: The Audit node uses a Temperature 0.0 setting to prevent creative or "guessed" medical advice.

Intent-Based Filtering: The model only focuses on relevant clinical markers, reducing irrelevant data processing.

🚀 How to Run
Add your GEMINI_API_KEY and NGROK_AUTH to your environment/secrets.

Install dependencies: pip install langchain-google-genai langgraph presidio-analyzer presidio-anonymizer spacy pdfplumber.

Run the Streamlit app and tunnel via Ngrok.
