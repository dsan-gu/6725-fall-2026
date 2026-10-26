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
| 4 | Advanced RAG | [sql-rag](https://github.com/gu-dsan6725/sql-rag) -- 100 pts + 50 bonus | [graph-rag](https://github.com/gu-dsan6725/graph-rag) -- 150 pts + 50 bonus, ANALYSIS.md carries 50 | Both shipped 2026-09-27; live Ollama smoke test pending |
| 5 | Introduction to Agents | [basic-agents](https://github.com/gu-dsan6725/basic-agents) -- 100 pts | -- | Shipped 2026-10-07, built for Fall 2026. Supersedes `agents` and `agents-part-2` (Spring carryover, now unused) |
| 6 | MCP and A2A | [agents-w-mcp](https://github.com/gu-dsan6725/agents-w-mcp) -- 200 pts | A2A: separate lab, TBD | Built and fully live-tested 2026-10-12, including part 3 against real Context7/GitHub keys. Servers run as standalone HTTP services; wire tap is a logging proxy; agents are Strands over the standard OpenAI-compatible client; same llama.cpp setup as week 5. Renamed from `mcp-a2a`; supersedes the `mcp-server`/`a2a-lab` placeholders |
| 7 | Evals and Observability | [evals-and-observability](https://github.com/gu-dsan6725/evals-and-observability) -- 200 pts | -- | Rebuilt from scratch and live-tested 2026-10-18 (OpenAI gpt-5-mini): part 1 traced agent on the keyless AWS Knowledge MCP server + Phoenix write-up; part 2 spec-only (no starter code) notes agent + phoenix-evals RAG/trajectory metrics, solutions implemented and verified. Students may use OpenAI, Anthropic, or local llama.cpp |
| 8 | Agent Evals in Practice | Continues week 7's assignment | -- | Deck built 2026-10-25: Meru trace-driven improvement case study + agent-sandboxes guest placeholder. No new lab |
| 9 | Tokenomics and Model Selection | TBD (new repo) | -- | Not started; deck now also carries open-weight vs frontier |
| 10 | Agentic Platforms | [agentic-ai-apps](https://github.com/gu-dsan6725/agentic-ai-apps) | -- | Spring carryover, needs review |
| 11 | Ontology and the Semantic Layer | TBD (new repo; Cypher and a real graph DB belong here) | -- | Moved from week 8; deck is Spring carryover, needs rebuild |
| 12 | Fine-tuning | [unsloth-finetune-ec2](https://github.com/gu-dsan6725/unsloth-finetune-ec2) | -- | Spring carryover, needs review |
| 13 | AI Ethics | -- | -- | No lab planned |
| 14 | Project Presentations | -- | Final project (max grade weight; abstract is a graded milestone) | Template: [final-project](https://github.com/gu-dsan6725/final-project) |

## Conventions every repo follows

- Instructor source repo holds everything; a top-level `solution/` folder is
  withheld from student copies by `create_repos.py`.
- Local models through Ollama (MiniCPM5-2B, nomic-embed-text) wherever they
  suffice; no API keys unless the work demands a frontier model. No Bedrock.
  **Exception, week 5**: `basic-agents` serves the same MiniCPM5-2B through
  `llama-server --jinja` instead of Ollama, because Ollama's template for that
  GGUF has no tool support and rejects any request carrying tools.
- Embedded engines over servers: DuckDB, Qdrant in-memory, networkx.
- `AGENTS.md` in every repo; prose follows the writing skill.
- A `check_submission.py` self-check where deliverables allow it; written
  reflections and analyses are always student-written, no AI.

## Working copies

Local clones for active development live in `.scratchpad/` (gitignored):
`sql-rag`, `graph-rag`, `lab01-agentic-coding`.
