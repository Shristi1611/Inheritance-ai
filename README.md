# The Inheritance

> A queryable memory you build for someone else.

They may be gone, but their voice isn't. The Inheritance lets you preserve a person's wisdom, stories, and voice — and have real conversations with them forever, powered by Cognee's permanent hybrid graph-vector memory layer.

---

## The Problem

When someone we love passes, we lose not just their presence but their accumulated wisdom. The advice they gave, the stories they told, the lessons they lived by. Every conversation is gone.

LLMs are stateless. They forget. Standard RAG resets every session.

What if that didn't have to be true?

---

## The Solution

The Inheritance uses Cognee's hybrid graph-vector memory layer to build a permanent, queryable knowledge graph from someone's words, voice notes, letters, and documents.

You feed it memories. It structures them into a graph. And then, across infinite sessions, you can ask questions and receive answers in their voice.

```python
# Feed a memory
await cognee.remember("Dad always said never sign a contract without sleeping on it.")

# Ask anything, across infinite sessions
answer = await cognee.recall("What did Dad say about contracts?")
# Returns: "Never sign a contract without sleeping on it. A deal that
# cannot wait until morning is not a deal worth making..."
```

---

## Features

- remember() -- Feed text, .txt files, and voice notes into the knowledge graph
- recall() -- Query memory with persona-aware responses that sound like the person
- improve() -- Enrich the graph over time as more memories are added
- forget() -- Surgically prune outdated or incorrect memories
- Voice transcription -- Upload audio files, auto-transcribed via Groq Whisper
- Animated UI -- Cinematic hero with spotlight reveal effect and chat interface

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Memory | Cognee (hybrid graph-vector) |
| LLM | Groq (llama-3.1-8b-instant) |
| Embeddings | FastEmbed (sentence-transformers/all-MiniLM-L6-v2) |
| Voice | Groq Whisper |
| Backend | FastAPI + Python |
| Frontend | Vanilla HTML/CSS/JS |

---

## Getting Started

### Prerequisites

- Python 3.10+
- Groq API key (free at console.groq.com)

### Installation

```bash
git clone https://github.com/Shristi1611/Inheritance-ai.git
cd Inheritance-ai

pip install cognee fastapi uvicorn groq python-dotenv python-multipart aiofiles
pip install "cognee[fastembed]" fastembed
pip install "lancedb==0.17.0" "pyarrow==18.0.0"
```

### Configuration

Create a .env file:

```
OWNER_NAME=Dad

LLM_PROVIDER=groq
LLM_MODEL=groq/llama-3.1-8b-instant
LLM_API_KEY=your_groq_api_key_here

EMBEDDING_PROVIDER=fastembed
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_DIMENSIONS=384

COGNEE_SKIP_CONNECTION_TEST=true
ENABLE_BACKEND_ACCESS_CONTROL=false
```

### Run

```bash
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

---

## How to Use

1. Open the hero screen and choose who you are preserving (Dad, Mom, Grandparent...)
2. Click "Enter their world" to enter the chat interface
3. Feed memories in the sidebar -- type what they said, upload text files or voice notes
4. Ask anything and receive an answer in their voice

### Example

Feed this memory:
> Dad always said the best investment you can make is in yourself.

Then ask:
> What did Dad think about money?

And receive:
> Son, I always believed the best investment you can make is in yourself. Money comes and goes, but what you learn and who you become stays with you forever.

---

## Project Structure

```
Inheritance-ai/
├── core/
│   ├── config.py        # Configuration loader
│   ├── memory.py        # Cognee memory wrapper (remember/recall/improve/forget)
│   └── transcribe.py    # Groq Whisper voice transcription
├── api/
│   └── routes.py        # FastAPI endpoints
├── static/
│   └── index.html       # Full UI (hero + chat interface)
├── main.py              # FastAPI app entry point
├── requirements.txt
└── .env.example
```

---

## How Cognee Powers This

The Inheritance uses all four of Cognee's memory lifecycle APIs:

- cognee.remember() -- Ingests memories and structures them into a knowledge graph with entities, relationships, and summaries
- cognee.recall() -- Performs hybrid graph traversal and semantic search to find relevant memories
- cognee.improve() -- Re-runs graph enrichment to strengthen connections between memories over time
- cognee.forget() -- Surgically removes datasets when memories need to be updated or removed

The graph structure is what makes this powerful. It does not just store text -- it understands that "Dad's advice about contracts" connects to "Dad's philosophy on patience" connects to "Dad's business stories". A single question can traverse the entire knowledge graph and return a rich, contextual answer.

---

## Built for

The Hangover Part AI hackathon by WeMakeDevs x Cognee

---

## Author

Shristi Sinha -- github.com/Shristi1611