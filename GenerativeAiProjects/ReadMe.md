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

Skills Demonstrated: Session persistence, State checkpointing, and Contextual memory management.
