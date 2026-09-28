# Labs and Assignments by Week (Fall 2026)

The working tracker for what hands-on work ships each week. The student-facing
version lives on the course site ([docs/labs/index.md](docs/labs/index.md));
this file adds status and points. Repos in `gu-dsan6725` are private; students
receive per-student copies named `<repo>-<username>-fall-2026` via
[assignment-setup](https://github.com/dsan-gu/assignment-setup).

| Week | Lecture | Lab | Assignment / Bonus | Status |
|------|---------|-----|--------------------|--------|
| 1 | GenAI Foundations and Coding Assistants | [lab01-agentic-coding](https://github.com/gu-dsan6725/lab01-agentic-coding) -- 100 pts, reflection 50 | -- | Lab shipped, rebuilt for Fall 2026 |
| 2 | LLM Internals and Inference | [fm-inference](https://github.com/gu-dsan6725/fm-inference) -- 170 pts + 30 bonus | Bonus: NotebookLM podcast from the six papers, 25 pts (announced in the Week 2 deck) | Lab shipped |
| 3 | RAG and Agentic RAG | [basic-rag](https://github.com/gu-dsan6725/basic-rag) -- build, break, fix | -- | Lab shipped, rebuilt for Fall 2026 |
| 4 | Advanced RAG; MCP | [sql-rag](https://github.com/gu-dsan6725/sql-rag) -- 100 pts + 50 bonus | [graph-rag](https://github.com/gu-dsan6725/graph-rag) -- 150 pts + 50 bonus, ANALYSIS.md carries 50 | Both shipped 2026-09-27; live Ollama smoke test pending |
| 5 | Agent Architectures | [agents](https://github.com/gu-dsan6725/agents), [agents-part-2](https://github.com/gu-dsan6725/agents-part-2) | -- | Spring carryover, needs review |
| 6 | Evals, Observability, Guardrails | [evals-and-observability](https://github.com/gu-dsan6725/evals-and-observability) | -- | Spring carryover, needs review |
| 7 | Ontology and the Semantic Layer | TBD (new repo; Cypher and a real graph DB belong here) | -- | Not started |
| 8 | Tokenomics | TBD (new repo) | -- | Not started |
| 9 | Agentic Platforms | [agentic-ai-apps](https://github.com/gu-dsan6725/agentic-ai-apps) | -- | Spring carryover, needs review |
| 10 | Agent-to-Agent (A2A) | [a2a-lab](https://github.com/gu-dsan6725/a2a-lab) | -- | Spring carryover, needs review |
| 11 | Fine-tuning | [unsloth-finetune-ec2](https://github.com/gu-dsan6725/unsloth-finetune-ec2) | -- | Spring carryover, needs review |
| 12 | Open-Weight vs Frontier | TBD (self-hosting lab) | -- | Not started |
| 13 | AI Ethics | -- | -- | No lab planned |
| 14 | Project Presentations | -- | Final project (max grade weight; abstract is a graded milestone) | Template: [final-project](https://github.com/gu-dsan6725/final-project) |

## Conventions every repo follows

- Instructor source repo holds everything; a top-level `solution/` folder is
  withheld from student copies by `create_repos.py`.
- Local models through Ollama (MiniCPM5-2B, nomic-embed-text) wherever they
  suffice; no API keys unless the work demands a frontier model. No Bedrock.
- Embedded engines over servers: DuckDB, Qdrant in-memory, networkx.
- `AGENTS.md` in every repo; prose follows the writing skill.
- A `check_submission.py` self-check where deliverables allow it; written
  reflections and analyses are always student-written, no AI.

## Working copies

Local clones for active development live in `.scratchpad/` (gitignored):
`sql-rag`, `graph-rag`, `lab01-agentic-coding`.
