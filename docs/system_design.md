# Agentic AI System - System Design Document

## 1. Overview

This project implements a scalable multi-agent AI orchestration system capable of handling complex multi-step tasks using asynchronous workflows and specialized AI agents.

The system accepts a user request, decomposes it into smaller subtasks, coordinates execution across multiple agents, and streams progressive updates back to the user in real time.

Designed as a production-inspired multi-agent orchestration system showcasing async execution, streaming workflows, and scalable AI coordination.

The architecture focuses on:
- Asynchronous orchestration
- Scalability
- Fault tolerance
- Streaming communication
- Modular agent design

---

# 2. Tech Stack

- Python
- FastAPI
- AsyncIO
- WebSockets
- OpenAI API
- asyncio.Queue
- Uvicorn

---

# 3. Key Features

- Multi-agent orchestration
- Task decomposition
- Async workflow execution
- Real-time streaming responses
- Retry handling
- Queue-based communication
- Manual batching
- Fault-tolerant architecture

---

# 4. High-Level Architecture

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

The architecture is designed using modular components where each agent performs a specialized responsibility.

---

# 5. Core Components

## API Layer (FastAPI)

Handles:
- Incoming user requests
- Workflow triggering
- API responses
- WebSocket connections

Endpoints:
- POST `/execute`
- WebSocket `/ws`

---

## Workflow Orchestrator

Responsibilities:
- Manage agent execution
- Coordinate async workflows
- Aggregate outputs
- Handle execution sequencing

Implementation uses:

```python
asyncio.gather()
```

---

## Planner Agent

Responsibilities:
- Understand user intent
- Divide tasks into subtasks
- Assign subtasks to specialized agents

Example:

```python
[
    "retrieve information",
    "analyze data",
    "generate report"
]
```

---

## Retriever Agent

Responsibilities:
- Gather contextual information
- Simulate retrieval workflows
- Provide input data for downstream agents

---

## Analyzer Agent

Responsibilities:
- Analyze retrieved information
- Generate insights
- Produce intermediate outputs

---

## Writer Agent

Responsibilities:
- Aggregate outputs from agents
- Generate structured reports
- Produce final responses

---

# 6. Async Orchestration

The system uses Python asyncio for asynchronous orchestration.

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
- Better scalability
- Efficient resource utilization

---

# 7. Streaming Response Handling

Real-time updates are implemented using WebSockets.

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
- Progressive execution visibility
- Improved user experience

---

# 8. Queue-Based Communication

The architecture follows an event-driven communication model using asynchronous queues.

Responsibilities:
- Task coordination
- Decoupled execution
- Event-driven workflows
- Async communication between components

Current implementation:
- Python asyncio.Queue()

Future upgrade:
- Redis
- Kafka
- RabbitMQ

---

# 9. Retry Handling

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

# 10. Manual Batching

Custom batching logic is implemented independently using a BatchProcessor.

Purpose:
- Group tasks together
- Improve throughput
- Reduce processing overhead

This satisfies the manual batching requirement of the assignment.

---

# 11. Scalability Considerations

The system is designed with scalability in mind.

Implemented scalability features:
- Async execution
- Concurrent agent processing
- Queue-based workflows
- Streaming responses
- Decoupled architecture
- Retry handling
- Manual batching

---

# 12. Scaling Issue Encountered

Managing multiple concurrent WebSocket streaming connections while coordinating asynchronous agent execution increased event-loop overhead during development.

As the number of active streaming clients increased, synchronization and resource management became more challenging.

---

# 13. Design Decision to Improve

Future versions would replace local asyncio queues with distributed messaging systems such as Kafka or RabbitMQ.

Advantages:
- Persistent messaging
- Distributed scalability
- Better fault tolerance
- Horizontal scaling support

---

# 14. Development Trade-offs

Redis and Docker integration were simplified into Python asyncio queues to reduce setup complexity and accelerate prototype development.

This trade-off enabled faster development while still demonstrating asynchronous event-driven workflows.

---

# 15. API Example

## Request

```json
{
  "task": "Generate AI investment report"
}
```

## Response

```json
{
  "report": "AI Investment Report..."
}
```

---

# 16. Engineering Highlights

This project demonstrates core software engineering and distributed systems concepts through a modular multi-agent AI architecture.

Key engineering strengths include:
- Asynchronous workflow orchestration
- Real-time streaming communication
- Event-driven architecture
- Modular agent boundaries
- Fault-tolerant execution
- Queue-based coordination
- Concurrent task processing
- Scalable system design
- Manual batching implementation
- Clean separation of responsibilities

The system was intentionally designed without relying on black-box agent frameworks in order to demonstrate low-level orchestration, async coordination, and system design understanding.

---

# 17. Future Improvements

- Kafka integration
- RabbitMQ integration
- Distributed worker nodes
- Persistent memory layer
- Monitoring and observability
- Authentication support
- Kubernetes deployment

---

# 18. Conclusion

This project successfully demonstrates a scalable Agentic AI orchestration system capable of handling complex multi-step tasks using asynchronous execution, specialized AI agents, streaming responses, retry handling, queue-based communication, and manual batching.
