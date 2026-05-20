# Agentic AI System for Multi-Step Tasks

A scalable multi-agent AI orchestration system built using FastAPI, asyncio, WebSockets, and asynchronous workflow execution.

This project demonstrates task decomposition, multi-agent coordination, streaming responses, retry handling, queue-based communication, and manual batching for scalable AI workflows.

---

# Project Overview

The system accepts complex user requests, decomposes them into smaller executable subtasks, assigns those tasks to specialized AI agents, coordinates asynchronous execution, and streams progressive updates back to the user in real time.

The architecture is designed with:
- Scalability
- Fault tolerance
- Async orchestration
- Streaming communication
- Modular agent boundaries

---

# Key Features

- Multi-agent orchestration
- Planner Agent for task decomposition
- Retriever Agent for information gathering
- Analyzer Agent for processing and insights
- Writer Agent for final response generation
- Async workflow execution using asyncio
- WebSocket-based streaming responses
- Queue-based communication
- Retry handling mechanisms
- Manual batching implementation
- Fault-tolerant architecture

---

# Tech Stack

- Python
- FastAPI
- AsyncIO
- WebSockets
- OpenAI API (optional)
- asyncio.Queue
- Uvicorn

---

# Architecture

```text
User Request
      │
      ▼
FastAPI API Layer
      │
      ▼
Workflow Orchestrator
      │
      ▼
Planner Agent
      │
 ┌────┴─────────────┐
 ▼                  ▼
Retriever Agent   Analyzer Agent
        │            │
        └────┬───────┘
             ▼
        Writer Agent
             │
             ▼
Streaming Response (WebSocket)
```

---

# Core Components

## API Layer

Handles:
- Incoming requests
- Workflow triggering
- API responses
- WebSocket connections

Endpoints:
- `POST /execute`
- `WebSocket /ws`

---

## Workflow Orchestrator

Coordinates:
- Async execution
- Agent communication
- Workflow sequencing
- Output aggregation

Uses:

```python
asyncio.gather()
```

for concurrent execution.

---

## Planner Agent

Responsibilities:
- Understand user intent
- Break tasks into subtasks
- Assign subtasks to agents

---

## Retriever Agent

Responsibilities:
- Gather contextual information
- Simulate retrieval workflows
- Prepare input data

---

## Analyzer Agent

Responsibilities:
- Analyze retrieved data
- Generate insights
- Produce intermediate outputs

---

## Writer Agent

Responsibilities:
- Aggregate outputs
- Generate structured reports
- Produce final responses

---

# Async Orchestration

The system uses asynchronous execution for scalability and concurrency.

Example:

```python
await asyncio.gather(
    retriever_task,
    analyzer_task
)
```

Benefits:
- Concurrent task execution
- Reduced latency
- Efficient resource usage
- Improved scalability

---

# Streaming Response Handling

WebSocket-based streaming provides real-time updates during execution.

Example streamed messages:

```text
Planning tasks...
Retriever Agent completed
Analyzer Agent completed
Writer Agent completed
Final report generated
```

Benefits:
- Real-time feedback
- Better user experience
- Progressive execution visibility

---

# Queue-Based Communication

The architecture uses asynchronous queues for event-driven communication.

Current implementation:
- Python asyncio.Queue()

Future support:
- Redis
- Kafka
- RabbitMQ

---

# Retry Handling

Fault tolerance is implemented using retry mechanisms.

Features:
- Automatic retries
- Configurable retry count
- Delay between retries

Benefits:
- Improved resilience
- Better reliability
- Reduced transient failures

---

# Manual Batching

Custom batching logic is implemented independently using a BatchProcessor.

Purpose:
- Group tasks together
- Improve throughput
- Reduce processing overhead

This satisfies the manual batching requirement of the assignment.

---

# Engineering Highlights

- Built asynchronous multi-agent orchestration system using Python asyncio
- Implemented concurrent workflow execution using asyncio.gather()
- Designed event-driven communication architecture
- Added real-time streaming updates using WebSockets
- Implemented retry handling for fault tolerance
- Developed custom manual batching logic
- Built modular agent-based architecture
- Designed scalable workflow orchestration pipeline

---

# Project Structure

```text
agentic-ai-system/
│
├── agents/
│   ├── planner_agent.py
│   ├── retriever_agent.py
│   ├── analyzer_agent.py
│   └── writer_agent.py
│
├── api/
│   └── main.py
│
├── orchestrator/
│   └── workflow.py
│
├── streaming/
│   └── websocket_manager.py
│
├── retry/
│   └── retry_handler.py
│
├── batching/
│   └── batch_processor.py
│
├── queue/
│   └── redis_queue.py
│
├── docs/
│   └── system_design.md
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Server

```bash
uvicorn api.main:app --reload
```

---

# API Testing

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# WebSocket Streaming

Connect using:

```text
ws://127.0.0.1:8000/ws
```

---

# Example API Request

```json
{
  "task": "Generate AI investment report"
}
```

---

# Example API Response

```json
{
  "report": "AI Investment Report..."
}
```
## Redis Queue Integration

The system integrates Redis for asynchronous task queue simulation.

Run Redis using Docker:

```bash
docker run -d -p 6379:6379 redis
```

Check running containers:

```bash
docker ps
```

Redis improves scalability and asynchronous communication between agents.
---

# Scalability Considerations

Implemented scalability features:
- Async execution
- Concurrent agent processing
- Queue-based workflows
- Streaming communication
- Retry handling
- Manual batching
- Decoupled architecture

---

# Scaling Issue Encountered

Managing multiple concurrent WebSocket streaming connections while coordinating asynchronous agent execution increased event-loop overhead during development.

---

# Design Decision to Improve

Future versions would replace local asyncio queues with distributed messaging systems such as Kafka or RabbitMQ.

---

# Development Trade-offs

Redis/Docker integration was simplified into Python asyncio queues to reduce setup complexity and accelerate prototype development.

---

# Future Improvements

- Kafka integration
- RabbitMQ integration
- Distributed worker nodes
- Persistent memory layer
- Monitoring and observability
- Authentication support
- Kubernetes deployment

---

# Conclusion

This project demonstrates a scalable Agentic AI orchestration system capable of handling complex multi-step tasks using asynchronous execution, specialized AI agents, streaming responses, retry handling, queue-based communication, and manual batching.

---

# Author

Srinidhi Kasam
