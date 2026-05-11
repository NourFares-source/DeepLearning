🌿 Gardener AI: Multi-Node Plant Health Assistant
Gardener AI is an agentic, multimodal application designed to monitor plant health over time. It uses a sequenced node-based architecture to combine real-time environmental data with computer vision to provide a "medical record" for your plants.

Built specifically to overcome local infrastructure limitations, it features a custom JSON-based persistence layer to ensure reliability in notebook-hosted environments.

🚀 Core Features
Multimodal Analysis: Utilizes Gemini 2.0 Flash to perform visual audits of plant health.

Hyperlocal Context: Integrates the OpenWeather API and browser-based geolocation to factor in temperature and humidity.

Session Persistence: Features a custom-built JSON Medical Record system that tracks a plant's health history across multiple sessions.

Logic-Based Prescription: A dedicated decision node determines if a plant requires medication or routine changes.

Mobile-Ready Tunneling: Integrated with Ngrok to allow secure camera and GPS access on mobile devices.

🏗️ The Agentic Architecture
The application is structured into three distinct functional nodes that pass a state dictionary:

Environment Node: Fetches local weather and location metadata.

Visual Expert Node: Analyzes images for pests or deficiencies while comparing them to historical logs.

Prescription Node: Evaluates the AI's findings to trigger specific health alerts or "medication due" statuses.

🛠️ Tech Stack
LLM: Google Gemini 2.0 Flash.

Orchestration: Custom State-Management (Node-based).

UI Framework: Streamlit.

Persistence: JSON Serialization.

External APIs: OpenWeatherMap, Geopy.

Deployment: Ngrok Tunneling.

📋 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/gardener-ai.git
Set up Environment Variables/Secrets:

GEMINI_API_KEY: For plant identification and diagnosis.

OPENWEATHER_API_KEY: For hyperlocal climate data.

NGROK_AUTH: For public tunneling and camera access.

Run the application:

Bash
streamlit run app.py
💡 Resilience Engineering
During development, this project was optimized to handle specific environmental challenges:

Zero-Database Dependency: Replaced SQLite with JSON persistence to avoid library versioning conflicts common in cloud notebook environments.

API Robustness: Implemented exponential backoff and retry logic to handle temporary 503 "High Demand" errors from AI model backends.

Local Optimization: Configured fallbacks for location-restricted services to ensure functionality within the Lebanese technical landscape.
