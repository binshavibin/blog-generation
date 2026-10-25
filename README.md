# Blog Generation Agent

An agentic blog generator built with **LangGraph**, **LangChain**, and **Groq**, served through a **FastAPI** endpoint. Send a topic, and the agent writes an SEO-friendly title and then the full blog content in Markdown.

## How it works

The app runs a LangGraph workflow with two nodes in sequence:

```
START ──► title_creation ──► content_generation ──► END
```

| Node                 | What it does                                          |
| -------------------- | ----------------------------------------------------- |
| `title_creation`     | Generates an SEO-friendly blog title for the topic    |
| `content_generation` | Writes the blog body in Markdown for the same topic   |

The LLM is Groq's `openai/gpt-oss-20b`, called through `langchain-groq`. If you set a LangSmith key, runs are traced in LangSmith.

## Project structure

```
blog-generatiion/
├── app.py                    # FastAPI app and /blogs endpoint
├── src/
│   ├── graphs/
│   │   └── graph_builder.py  # Builds and compiles the LangGraph workflow
│   ├── llms/
│   │   └── groq_llm.py       # Groq chat model setup
│   ├── nodes/
│   │   └── blog_node.py      # Title and content generation nodes
│   └── states/
│       └── blog_state.py     # BlogState and Blog schema
├── request.json              # Sample request body
├── pyproject.toml            # Project metadata and dependencies (uv)
├── uv.lock                   # Locked dependency versions
└── requirements.txt          # Dependencies for pip users
```

## Prerequisites

- Python 3.11 or newer
- A [Groq API key](https://console.groq.com/keys)
- (Optional) A [LangSmith API key](https://smith.langchain.com/) for tracing
- (Optional) [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd blog-generatiion
```

### 2. Install dependencies

**With uv (recommended):**

```bash
uv sync
```

**With pip:**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=blog-generation
```

> `.env` is listed in `.gitignore`, so your keys are never committed.

## Running the app

```bash
# with uv
uv run python app.py

# or with an activated virtual environment
python app.py
```

The server starts at `http://localhost:8000` with auto-reload turned on. Interactive API docs are at `http://localhost:8000/docs`.

## API usage

### `POST /blogs`

Generates a blog for the given topic.

**Request body**

```json
{
  "topic": "Agentic AI"
}
```

**Example with curl**

```bash
curl -X POST http://localhost:8000/blogs \
  -H "Content-Type: application/json" \
  -d @request.json
```

**Example response**

```json
{
  "data": {
    "topic": "Agentic AI",
    "blog": {
      "title": "# Agentic AI: How Autonomous Agents Are Changing Software",
      "content": "## Introduction\n..."
    }
  }
}
```

## Tech stack

- [LangGraph](https://langchain-ai.github.io/langgraph/): workflow orchestration
- [LangChain](https://python.langchain.com/): LLM integration
- [Groq](https://groq.com/): fast LLM inference
- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/): API server
- [LangSmith](https://smith.langchain.com/): tracing (optional)

## Roadmap

- [ ] Multi-language blog generation (the `content_language` field already exists in `BlogState`)
- [ ] Input validation with a Pydantic request model
- [ ] Error response when `topic` is missing
