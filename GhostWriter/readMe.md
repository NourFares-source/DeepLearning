🕵️‍♂️ Sherlock GhostWriter: AI-Powered Style Mimicry
This project is a sophisticated GhostWriting Engine built using LangGraph and Llama 3.1. It analyzes the linguistic "DNA" of a specific author—in this case, Sherlock Holmes—to generate new content that mimics their unique writing style, vocabulary, and deductive tone.

🚀 Key Features
Linguistic Collector Node: Uses K-Means Clustering and Sentence Transformers (all-MiniLM-L6-v2) to identify the most representative style samples from a source text.

Style DNA Profiling: Leverages Groq (Llama 3.1) to perform a deep structural analysis of the author's prose, focusing on sentence complexity, imagery, and tone.

Iterative Generation: Implements a state-based workflow where the AI writes content based on a "Style Guide" derived from actual source data.

Memory Persistence: Utilizes MemorySaver to maintain the context of the style analysis across multiple user queries.

🏗️ Technical Architecture
The engine is built as a directed acyclic graph (DAG) using LangGraph:

Collector Node: Splits the source .txt file into chunks and filters out metadata/legal noise.

Analysis Node: Generates a comprehensive "Style DNA" string.

Generation Node: Produces a response to a user-defined topic using the analyzed style constraints.

🛠️ Tech Stack
Orchestration: LangGraph

LLM Provider: Groq Cloud (Llama-3.1-8b-instant & Llama-3.3-70b-versatile)

Embeddings: Hugging Face Sentence-Transformers

Data Science: Scikit-Learn (K-Means), NumPy, Pandas
