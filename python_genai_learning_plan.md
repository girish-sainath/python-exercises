# Python Learning Plan: Building Blocks for Generative AI, Agentic AI & MCP Development

## Overview

This plan takes you from Python fundamentals to production-ready expertise in GenAI, Agentic AI, and Model Context Protocol (MCP) development. It is structured in five progressive phases, each building on the last.

**Total estimated time:** 20–30 weeks (part-time, ~10–15 hrs/week)

---

## Phase 1: Python Foundations (Weeks 1–4)

> **Goal:** Write clean, idiomatic Python that you can build AI applications on top of.

### 1.1 Core Language

| Topic | Key Concepts | Resources |
|---|---|---|
| Data types & structures | `list`, `dict`, `set`, `tuple`, comprehensions | Official Python docs |
| Functions | `*args`, `**kwargs`, closures, decorators | "Fluent Python" by Ramalho |
| Classes & OOP | `__init__`, inheritance, `@property`, `dataclass` | Real Python tutorials |
| Error handling | `try/except/finally`, custom exceptions | Python docs |
| File I/O & context managers | `with` statement, `pathlib`, JSON/CSV | Real Python |

### 1.2 Intermediate Python

| Topic | Key Concepts |
|---|---|
| Type hints & annotations | `typing` module, `Optional`, `Union`, `Literal`, `TypedDict` |
| Iterators & generators | `yield`, `yield from`, lazy evaluation |
| Functional tools | `map`, `filter`, `functools.partial`, `itertools` |
| String manipulation | f-strings, `re` module, template strings |
| `dataclasses` & `pydantic` | Structured data modeling, validation |

### 1.3 Python Ecosystem

- **Package management:** `pip`, `venv`, `pyproject.toml`, `uv` (fast modern tooling)
- **Linting/formatting:** `ruff`, `black`, `mypy`
- **Testing basics:** `pytest`, fixtures, mocking with `unittest.mock`
- **Logging:** `logging` module, structured logging

### Milestone Project
Build a CLI tool that reads a JSON config file, validates it with Pydantic, and outputs a formatted report. Covers: I/O, Pydantic, type hints, CLI with `argparse` or `typer`.

---

## Phase 2: Async Python & APIs (Weeks 5–8)

> **Goal:** Master async programming and HTTP APIs — both essential for AI workloads.

### 2.1 Asynchronous Python

| Topic | Key Concepts |
|---|---|
| Event loop fundamentals | `asyncio`, `await`, `async def` |
| Concurrency patterns | `asyncio.gather`, `asyncio.create_task`, `asyncio.Queue` |
| Async context managers | `async with`, `__aenter__`/`__aexit__` |
| Async generators | `async for`, `async yield` |
| Timeouts & cancellation | `asyncio.wait_for`, `asyncio.CancelledError` |
| Mixing sync & async | `asyncio.run_in_executor`, `anyio` |

### 2.2 HTTP & API Clients

| Topic | Key Concepts |
|---|---|
| `httpx` | Async HTTP client, headers, auth, streaming responses |
| REST API consumption | Query params, request/response cycles, pagination |
| Server-sent events (SSE) | Streaming responses from LLMs |
| WebSockets | Real-time bidirectional communication |
| Rate limiting & retries | `tenacity` library, exponential backoff |

### 2.3 Building APIs with FastAPI

| Topic | Key Concepts |
|---|---|
| Route definitions | `@app.get`, `@app.post`, path/query params |
| Request/response models | Pydantic integration |
| Dependency injection | `Depends`, shared state |
| Streaming responses | `StreamingResponse`, SSE endpoints |
| Background tasks | `BackgroundTasks`, async workers |
| OpenAPI docs | Auto-generated Swagger UI |

### Milestone Project
Build a FastAPI server that proxies requests to the Claude API with streaming, rate limiting, and request logging. Covers: async, SSE, httpx, FastAPI, Pydantic.

---

## Phase 3: LLM & Generative AI Fundamentals (Weeks 9–13)

> **Goal:** Build fluency with LLMs programmatically — prompting, tool use, and RAG patterns.

### 3.1 Anthropic Claude API

| Topic | Key Concepts |
|---|---|
| Messages API | `messages.create`, roles, content blocks |
| Model selection | Claude 4.x family — Haiku (fast/cheap), Sonnet (balanced), Opus (most capable) |
| Prompt engineering | System prompts, few-shot examples, chain-of-thought |
| Token counting | `count_tokens`, context window management |
| Streaming | `stream=True`, event types, `MessageStream` |
| Vision | Image content blocks, base64 and URL inputs |
| Structured output | `tool_use` for forcing JSON schemas |

```python
# Example: Streaming with the Anthropic SDK
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain async Python in 3 sentences."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### 3.2 Tool Use (Function Calling)

| Topic | Key Concepts |
|---|---|
| Defining tools | JSON Schema definitions for tool input |
| Tool use loop | Detecting `tool_use` blocks, executing, returning `tool_result` |
| Parallel tool use | Multiple tools in one response |
| Forced tool use | `tool_choice` parameter |
| Error handling | Returning errors as `tool_result` |

```python
# Tool definition pattern
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and country"},
            },
            "required": ["location"],
        },
    }
]
```

### 3.3 Prompt Caching & Optimization

| Topic | Key Concepts |
|---|---|
| Prompt caching | `cache_control` headers, cache breakpoints |
| Cost optimization | Cache hit ratios, when caching pays off |
| Batch API | Async batch processing for offline workloads |
| Token efficiency | Minimizing prompt tokens, reuse patterns |

### 3.4 Embeddings & Retrieval-Augmented Generation (RAG)

| Topic | Key Concepts |
|---|---|
| Embeddings concepts | Vector representations, cosine similarity |
| Generating embeddings | `voyage-4`, `voyage-code-3` via Voyage AI |
| Vector stores | In-memory with `numpy`, `faiss`, `chromadb`, `pgvector` |
| Chunking strategies | Fixed-size, semantic, recursive splitting |
| Retrieval patterns | Similarity search, MMR, hybrid search |
| Reranking | Cross-encoder reranking, Cohere Rerank |
| RAG pipeline | Ingest → embed → store → retrieve → augment → generate |

### 3.5 MongoDB Atlas Vector Search (AI-Native Database)

| Topic | Key Concepts |
|---|---|
| Atlas Vector Search | Creating vector search indexes, `$vectorSearch` aggregation |
| Semantic search | Embedding documents and querying by vector similarity |
| Hybrid search | Combining vector + full-text search |
| Metadata filtering | Pre-filtering with Atlas Search |
| MongoDB MCP integration | Using MongoDB as a tool/data source for AI agents |

```python
# Example: Vector search with MongoDB
pipeline = [
    {
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 100,
            "limit": 10
        }
    },
    {"$project": {"text": 1, "score": {"$meta": "vectorSearchScore"}}}
]
```

### Milestone Project
Build a document Q&A system: ingest PDFs, chunk and embed content into MongoDB Atlas, retrieve relevant chunks, and answer questions using Claude with citations.

---

## Phase 4: Agentic AI & Agent Frameworks (Weeks 14–19)

> **Goal:** Build autonomous agents that reason, plan, and execute multi-step tasks.

### 4.1 Agent Fundamentals

| Topic | Key Concepts |
|---|---|
| ReAct pattern | Reason → Act → Observe loop |
| Agent loop | LLM call → parse action → execute tool → feed result back |
| Memory types | In-context (scratchpad), external (vector store), episodic |
| Planning strategies | Chain-of-thought, tree-of-thought, LATS |
| Stopping conditions | Max steps, goal achieved, error thresholds |

```python
# Minimal agent loop pattern
def run_agent(task: str, tools: list, max_steps: int = 10):
    messages = [{"role": "user", "content": task}]
    
    for _ in range(max_steps):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            tools=tools,
            messages=messages,
        )
        
        if response.stop_reason == "end_turn":
            return response  # Agent finished
        
        if response.stop_reason == "tool_use":
            tool_results = execute_tools(response.content)
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
```

### 4.2 Anthropic Agent SDK

| Topic | Key Concepts |
|---|---|
| Agent primitives | `Agent`, `Runner`, tool definitions |
| Handoffs | Passing control between specialized agents |
| Guardrails | Input/output validation, tripwires |
| Lifecycle hooks | `on_tool_start`, `on_tool_end`, tracing |
| Streaming agents | Real-time output from long-running agents |
| Context management | Passing state between turns |

### 4.3 Multi-Agent Architectures

| Topic | Key Concepts |
|---|---|
| Orchestrator pattern | One agent coordinates specialist sub-agents |
| Parallel agent execution | Fan-out tasks to concurrent agents |
| Agent-as-tool | Calling one agent from another via tool |
| Supervisor pattern | Monitor agent quality, trigger retries |
| Swarm / debate patterns | Multiple agents refine the same answer |

```
Orchestrator Agent
├── Research Agent (web search + summarization)
├── Code Agent (writes + executes code)
├── Critic Agent (reviews and improves)
└── Writer Agent (final synthesis)
```

### 4.4 Memory & State Management

| Topic | Key Concepts |
|---|---|
| Conversation memory | Summarization, sliding window, compression |
| Semantic memory | Embeddings-based long-term recall |
| Episodic memory | Storing and retrieving past interactions |
| Working memory | Scratchpad patterns, chain-of-thought externalization |
| Persistence | MongoDB, Redis, SQLite for agent state |

### 4.5 Tool Design & Security

| Topic | Key Concepts |
|---|---|
| Tool design principles | Narrow scope, clear descriptions, idempotency |
| Input validation | Pydantic models for tool inputs |
| Sandboxing | Isolating code execution, filesystem limits |
| Prompt injection defense | Untrusted content handling, input sanitization |
| Observability | Tracing tool calls, logging agent decisions |

### 4.6 Computer Use & Long-Running Agents

| Topic | Key Concepts |
|---|---|
| Computer use API | Screenshot, click, type, scroll actions |
| Human-in-the-loop | Approval flows, interruption points |
| Checkpointing | Save/restore agent state mid-task |
| Error recovery | Retry logic, fallback strategies |

### Milestone Project
Build a research agent that:
1. Accepts a research question
2. Searches the web and internal documents (RAG)
3. Delegates sub-questions to specialist agents
4. Synthesizes a structured report with citations
5. Stores findings in MongoDB for future retrieval

---

## Phase 5: Model Context Protocol (MCP) (Weeks 20–25)

> **Goal:** Build MCP servers and clients to extend AI assistants with custom tools and data sources.

### 5.1 MCP Architecture & Concepts

| Topic | Key Concepts |
|---|---|
| Protocol overview | Client ↔ Server communication model |
| Transport layers | stdio (local), SSE (remote), WebSocket |
| Primitives | **Tools** (actions), **Resources** (data), **Prompts** (templates) |
| Lifecycle | Initialize → capability negotiation → request/response |
| JSON-RPC 2.0 | The underlying protocol format |

```
MCP Host (Claude Desktop / Claude Code)
    │
    ├── MCP Client
    │       │
    │       ├── MCP Server A (filesystem tools)
    │       ├── MCP Server B (your custom server)
    │       └── MCP Server C (MongoDB MCP)
```

### 5.2 Building MCP Servers with Python SDK

```python
# Minimal MCP server
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def calculate_sum(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.resource("data://config")
def get_config() -> str:
    """Return application configuration."""
    return '{"version": "1.0", "env": "production"}'

@mcp.prompt()
def analysis_prompt(topic: str) -> str:
    """Generate an analysis prompt for a given topic."""
    return f"Analyze the following topic in depth: {topic}"

if __name__ == "__main__":
    mcp.run()
```

| Topic | Key Concepts |
|---|---|
| `FastMCP` decorator API | `@mcp.tool()`, `@mcp.resource()`, `@mcp.prompt()` |
| Tool definitions | Type hints auto-generate JSON Schema |
| Resource URIs | URI templates, dynamic resources |
| Prompt templates | Parameterized prompts for reuse |
| Server configuration | Name, version, capabilities |

### 5.3 Advanced MCP Server Patterns

| Topic | Key Concepts |
|---|---|
| Async tools | `async def` tool handlers |
| Streaming resources | Large data resources via chunked responses |
| Resource subscriptions | Server-sent change notifications |
| Sampling (LLM calls) | Server-side LLM calls back through the host |
| Roots & filesystem access | Declaring accessible paths |
| Authentication | OAuth 2.0, API key patterns for remote servers |

```python
# Async tool with external API call
@mcp.tool()
async def search_documents(query: str, limit: int = 10) -> list[dict]:
    """Search internal document store by semantic similarity."""
    async with httpx.AsyncClient() as client:
        embeddings = await get_embeddings(query)
        results = await vector_search(embeddings, limit)
        return results
```

### 5.4 MCP Transport Layers

| Transport | Use Case | Key Details |
|---|---|---|
| **stdio** | Local servers (Claude Desktop, Claude Code) | Process stdin/stdout |
| **SSE (HTTP)** | Remote/cloud servers | Server-sent events over HTTP |
| **WebSocket** | Bidirectional real-time remote | Persistent connection |

```python
# SSE transport for remote deployment
if __name__ == "__main__":
    import uvicorn
    from mcp.server.sse import SseServerTransport
    
    # Expose as HTTP SSE endpoint
    mcp.run(transport="sse", host="0.0.0.0", port=8080)
```

### 5.5 MCP Client Development

| Topic | Key Concepts |
|---|---|
| `ClientSession` | Connecting to MCP servers |
| Listing capabilities | `list_tools()`, `list_resources()`, `list_prompts()` |
| Calling tools | `call_tool(name, arguments)` |
| Reading resources | `read_resource(uri)` |
| Using prompts | `get_prompt(name, arguments)` |
| Multi-server clients | Aggregating tools from multiple servers |

```python
# MCP client usage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def use_mcp_server():
    server_params = StdioServerParameters(
        command="python", args=["my_server.py"]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            result = await session.call_tool("calculate_sum", {"a": 3, "b": 4})
            print(result)
```

### 5.6 Production MCP Patterns

| Topic | Key Concepts |
|---|---|
| Error handling | MCP error codes, graceful degradation |
| Logging & tracing | Structured logs, request IDs |
| Security | Input sanitization, authorization, secret management |
| Testing MCP servers | `mcp dev` inspector, unit testing handlers |
| Deployment | Docker containers, cloud functions, `npx @modelcontextprotocol/inspector` |
| Configuration | `claude_desktop_config.json` integration |

### 5.7 MongoDB MCP Server

The MongoDB MCP server is a production-grade example to study and extend:

| Feature | Description |
|---|---|
| Natural language queries | Translate questions into MongoDB aggregations |
| Schema inspection | `collection-schema` and `collection-indexes` tools |
| Vector search integration | `$vectorSearch` via `aggregate` tool |
| Atlas Search | Full-text search with the `search` tool |
| Multi-database support | Works with any MongoDB Atlas cluster |

### Milestone Project
Build a complete MCP server that:
1. Exposes MongoDB collections as **resources**
2. Provides semantic search as a **tool** (with Atlas Vector Search)
3. Includes **prompt templates** for common data analysis tasks
4. Supports both stdio and SSE transports
5. Integrates with Claude Desktop and Claude Code

---

## Phase 6: Production & Advanced Topics (Weeks 26–30)

> **Goal:** Ship reliable, observable, and maintainable AI systems.

### 6.1 Observability & Evaluation

| Topic | Key Concepts |
|---|---|
| Tracing agent runs | OpenTelemetry, Langfuse, Weave |
| Evaluating LLM outputs | LLM-as-judge, structured evals |
| Regression testing | Snapshot tests for prompts |
| Cost tracking | Token usage dashboards, budget alerts |
| Latency profiling | P50/P99 response times, bottleneck identification |

### 6.2 Reliability Patterns

| Topic | Key Concepts |
|---|---|
| Retry logic | `tenacity`, exponential backoff with jitter |
| Circuit breakers | Prevent cascade failures |
| Fallback models | Degrading to cheaper/faster models |
| Prompt versioning | Tracking prompt changes like code |
| Caching strategies | Semantic caching, exact-match caching |

### 6.3 Security for AI Systems

| Topic | Key Concepts |
|---|---|
| Prompt injection | Input validation, content filtering |
| Data exfiltration | Output scanning, PII detection |
| Tool sandboxing | Restricting what agents can access |
| Secret management | Never put secrets in prompts |
| Supply chain | Validating MCP servers before use |

### 6.4 Deployment

| Topic | Key Concepts |
|---|---|
| Containerization | Docker, multi-stage builds |
| Serverless | AWS Lambda, Google Cloud Run for MCP servers |
| Configuration management | `pydantic-settings`, env-based config |
| CI/CD | GitHub Actions for automated testing |

---

## Recommended Learning Resources

### Books
- **"Fluent Python" (2nd Ed.)** — Luciano Ramalho — Deep Python mastery
- **"Architecture Patterns with Python"** — Percival & Gregory — Async patterns, clean architecture
- **"Designing Machine Learning Systems"** — Chip Huyen — Production ML context

### Official Documentation (always primary source)
- [Anthropic API Docs](https://docs.anthropic.com) — Claude API, tool use, streaming
- [MCP Specification](https://modelcontextprotocol.io) — Full protocol spec
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) — Reference implementation
- [FastAPI Docs](https://fastapi.tiangolo.com) — Async API framework
- [Pydantic Docs](https://docs.pydantic.dev) — Data validation

### Practice
- Build projects, don't just read — each phase has a milestone project
- Study the [MongoDB MCP server](https://github.com/mongodb-js/mongodb-mcp-server) source as a production MCP reference
- Read the [Anthropic Claude Code](https://github.com/anthropics/claude-code) source for agent loop patterns

---

## Weekly Schedule Template

```
Monday    — Concept study (1–2 hrs): read docs, watch talks
Tuesday   — Hands-on coding (2–3 hrs): implement the day's topic
Wednesday — Hands-on coding continued
Thursday  — Review & refactor previous code (1 hr)
Friday    — Milestone project work (2–3 hrs)
Weekend   — Milestone project wrap-up or rest
```

---

## Skills Checklist

### Python Foundations
- [ ] Write type-annotated Python with Pydantic models
- [ ] Use generators and async generators effectively
- [ ] Implement custom decorators and context managers

### Async & APIs
- [ ] Build a streaming FastAPI endpoint
- [ ] Handle SSE (server-sent events) in both client and server
- [ ] Implement retry logic with exponential backoff

### LLMs & GenAI
- [ ] Implement a full tool-use loop with Claude
- [ ] Build a RAG pipeline from scratch
- [ ] Use Atlas Vector Search for semantic retrieval
- [ ] Optimize costs with prompt caching

### Agentic AI
- [ ] Implement a ReAct agent loop from scratch
- [ ] Build a multi-agent orchestrator
- [ ] Handle agent errors and recovery gracefully

### MCP
- [ ] Build an MCP server with tools, resources, and prompts
- [ ] Deploy an MCP server over SSE transport
- [ ] Write an MCP client that calls multiple servers
- [ ] Integrate a custom MCP server with Claude Desktop

---

*Last updated: June 2026*
