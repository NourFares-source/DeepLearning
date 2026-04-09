📂 Repository Summary: LangGraph Agentic Workflows
A collection of advanced stateful AI systems demonstrating orchestration, persistence, and human-machine collaboration.

1. Self-Correcting Data Agent (SQL-LLM)
Concept: A natural language interface for databases that translates user queries into executable SQL code.

Technical Implementation: Built using a ReAct logic loop that connects an LLM to a SQLite backend.

Key Innovation: Developed a self-healing mechanism where the agent captures database execution errors and tracebacks, autonomously reflecting on the failure to regenerate a corrected query without human intervention.

Skills Demonstrated: Error handling in LLMs, Database Logic, and Autonomous Loop design.

2. Multi-Agent Collaborative Auditor
Concept: A parallel processing system designed to audit complex documents (such as lease agreements) from multiple perspectives simultaneously.

Technical Implementation: Utilizes a "Fan-out/Fan-in" architecture where a Supervisor node broadcasts tasks to specialized "Tenant Advocate" and "Legal Compliance" agents.

Key Innovation: Engineered a centralized Synthesizer node that merges conflicting agent outputs into a unified, high-priority risk assessment report.

Skills Demonstrated: Multi-agent orchestration, Parallel state management, and Conflict resolution logic.

3. Persistent "Memory-Aware" Rental Assistant
Concept: A personalized recommendation engine that maintains long-term user context across separate interaction sessions.

4. Human-in-the-Loop (HITL) Supervisor
Concept: A high-stakes automation agent for professional communication that operates under a strict governance framework.

Technical Implementation: Employs manual interrupt breakpoints (interrupt_before) to freeze graph execution at critical action nodes.

Key Innovation: Designed a safety gate requiring explicit state updates and manual approvals before the agent can execute "real-world" tasks, such as dispatching emails or committing data.

Skills Demonstrated: AI Safety & Ethics, State manipulation, and Manual breakpoint orchestration.

Technical Implementation: Integrated LangGraph Checkpointers and MemorySaver to preserve state based on unique thread_id configurations.

Key Innovation: Implemented metadata extraction to store user preferences (budget, location, amenities) within the persistent state, enabling "zero-reprompt" personalization for returning users.

5. Automated MCQ Generator (PDF-to-Quiz)
Concept: An educational tool that transforms static documents into interactive learning materials.

Technical Implementation: Utilizes LangChain for document loading and text splitting, combined with an LLM to extract key concepts from PDFs.

Key Innovation: Designed structured output prompts to ensure the AI generates consistent, valid Multiple Choice Questions (MCQs) with correct answer keys and distractors.

Skills Demonstrated: PDF parsing, Data extraction, and Prompt Engineering for structured outputs.

6. "New Analyst" Data Agent
Concept: A virtual data analyst designed to assist with exploratory data analysis and insight generation.

Technical Implementation: Leverages Pandas and LLMs to interpret raw datasets and generate human-readable summaries.

Key Innovation: Implemented a logic flow that allows the agent to suggest relevant visualizations (using Seaborn/Matplotlib) based on the data types detected in the uploaded files.

Skills Demonstrated: Exploratory Data Analysis (EDA), Data interpretation, and Python-based data science workflows.

7. Formal vs. Casual Email Transformer
Concept: A communication assistant that adjusts the "tone" of professional correspondence while preserving the original intent.

Technical Implementation: Built using Few-Shot Prompting techniques to guide the LLM in recognizing the nuances between corporate formal and conversational casual styles.

Key Innovation: Created a comparative state where the user can view both versions simultaneously to choose the best fit for their audience.

Skills Demonstrated: NLP Style Transfer, Few-shot learning, and User-centric interface design.

Skills Demonstrated: Session persistence, State checkpointing, and Contextual memory management.
