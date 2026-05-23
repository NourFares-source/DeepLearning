# 🏛️ Smart City Environmental Sentinel (SentinelState)

A robust, multi-node data engineering pipeline and web application designed to evaluate urban air quality hazards using geospatial data. The application automates the transition from fragile human input data to real-time environmental telemetry sourced directly via Google Maps pinpoints and global climate APIs.

## 🛰️ Project Overview & Evolution

The project was developed using a rigorous, iterative architectural roadmap to transition from a conceptual pipeline into a bulletproof production utility.

### 🔹 Version 1.0: Proof of Concept
* Built a foundational 5-node architecture handling data ingestion, extraction, feature engineering, and analytics.
* Relied on raw, unstructured telemetry strings parsed via backend regex and splitters.

### 🔹 Version 1.1: Structured Collection & Persistence
* Removed text-parsing overhead by mapping structured HTML5 form payloads directly into an immutable application state
* dictionary (`SentinelState`).
* Implemented client-side type enforcement and boundary guardrails ($\ge 0.1$) to mathematically eliminate server-crashing
* `ZeroDivisionError` threats.
* Added a persistent, append-only local database layer using a thread-safe JSON ledger (`pollution_history.json`).

### 🔹 Version 1.2: Geospatial API Integration (Current Production)
* Eliminated user data-entry friction by reducing input down to a single Google Maps location link.
* Implemented a data parsing node using regular expressions to isolate latitude and longitude vectors from absolute and
* redirected URLs.
* Linked the data intake layer to the **OpenWeatherMap Air Pollution API** to stream real-time chemical compositions
*  dynamically.

* 

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.12+
* **Backend Framework:** Flask (WSGI Web Server Gateway Interface)
* **Frontend:** HTML5, CSS3 (Water.css Minimalist Framework), JavaScript (Asynchronous Fetch/AJAX API)
* **Data Core:** Python `TypedDict` structural types, Native JSON Ledger
* **Networking & Utilities:** `requests`, `re` (Regular Expressions), `uuid`, `datetime`
* **Development Environment:** Google Colab Ecosystem, `pyngrok` secure proxy tunneling

---

## 🚀 Installation & Local Deployment

### 1. Prerequisites
Ensure you have access to Google Colab or a local Python environment. You will need two external API keys:
1. **Ngrok Auth Token:** To proxy your local environment to a web address.
2. **OpenWeatherMap API Key:** A free account key to query the Air Pollution endpoint.

### 2. Environment Configuration
Securely register your API credentials into your environment variables or Google Colab **Secrets** utility (the 🔑 icon 
in the sidebar) using the exact keys below:
* `NGROK_AUTH` — *Your personal Ngrok token*
* `OPENWEATHER_KEY` — *Your OpenWeatherMap API key*

### 3. Execution
1. Run the HTML generator block to build the templates directory:
   ```bash
   mkdir -p templates
Run the main server script block inside your notebook or terminal.Access the public URL generated in the terminal
logs (*.ngrok-free.app) to open the web dashboard.📊 Core Analytical SignaturesThe evaluation engine detects specific urban 
polluters by computing derived molecular balances rather than relying purely on isolated indices:
Ratio A (Particulate Signature): $\text{PM}_{2.5} / (\text{Ozone} + \text{CO})
$Ratio B (Combustion Proximity): $(\text{NO}_2 + \text{CO}) / (\text{Ozone} + 1)
$Ratio C (Engine Profile): $\text{NO}_2 / (\text{CO} + 1)
$Target Diagnostic Triggers:High Particulate Matter Warning: Triggered when core values exceed 100 and Ratio A $> 1.2$
(Indicates soot, dust, or heavy industrial emissions).Heavy Diesel Traffic Warning: Triggered when Ratio B $> 1.5$ and 
Ratio C $> 1.0$ (Indicates high concentrations of diesel exhaust fumes requiring transit routing adjustments).
Photochemical Smog Alert: Triggered when Ratio B $< 0.5$ alongside high Ozone concentrations (Indicates stagnant regional
pollution baking in direct sunlight).


## 🏗️ System Architecture & Data Flow

The application utilizes a **Strict State Contract pattern** governed by Python `TypedDict` schemas. The data flows sequentially through detached functional nodes, maintaining a clear separation of concerns.
