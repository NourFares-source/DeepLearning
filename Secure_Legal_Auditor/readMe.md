# 🛡️ Secure Legal Auditor (LangGraph + Groq)

A high-performance RAG pipeline built with **LangGraph** and **Llama 3.3 (via Groq)** that prioritizes data accuracy and privacy.

## 🚀 Features
- **Multi-Stage Verification:** Uses a state-machine architecture to ensure summaries are grounded in truth.
- **Hallucination Detection:** Employs `Sentence-Transformers` and `Cosine Similarity` to mathematically verify AI claims against the source PDF.
- **Privacy Enforcement:** Integrated with **Microsoft Presidio** to automatically detect and redact PII (Names, Emails, Phones) before output.
- **Extreme Speed:** Powered by Groq's LPU inference engine.

## 🛠️ Tech Stack
- **Orchestration:** LangGraph
- **LLM:** Groq (Llama 3.3 70B)
- **Vector Audit:** Sentence-Transformers (all-MiniLM-L6-v2)
- **Privacy:** Microsoft Presidio
- **Parsing:** PyPDF2 & LangChain

## 📊 Verification Logic
1. **Extraction:** Recursive chunking of PDF text.
2. **Context Retrieval:** Targeted summary based on user query.
3. **Audit Gate:** If Cosine Similarity < 0.7, the system flags a potential hallucination.
4. **Redaction Gate:** Any detected PII is replaced with anonymized placeholders.
