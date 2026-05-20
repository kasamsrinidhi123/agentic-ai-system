# Agentic AI System - System Design Document

## 1. Overview

This project implements a scalable multi-agent AI orchestration system capable of handling complex multi-step tasks using asynchronous workflows and specialized AI agents.

The system accepts a user request, decomposes it into smaller subtasks, coordinates execution across multiple agents, and streams progressive updates back to the user in real time.

The architecture focuses on:
- Asynchronous orchestration
- Scalability
- Fault tolerance
- Streaming communication
- Modular agent design

---

# 2. High-Level Architecture

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

# 3. Core Components

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

# 4. Async Orchestration

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

# 5. Streaming Response Handling

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

# 6. Queue-Based Communication

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

# 7. Retry Handling

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

# 8. Manual Batching

Custom batching logic is implemented independently using a BatchProcessor.

Purpose:
- Group tasks together
- Improve throughput
- Reduce processing overhead

This satisfies the manual batching requirement of the assignment.

---

# 9. Scalability Considerations

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

# 10. Scaling Issue Encountered

Managing multiple concurrent WebSocket streaming connections while coordinating asynchronous agent execution increased event-loop overhead during development.

As the number of active streaming clients increased, synchronization and resource management became more challenging.

---

# 11. Design Decision to Improve

Future versions would replace local asyncio queues with distributed messaging systems such as Kafka or RabbitMQ.

Advantages:
- Persistent messaging
- Distributed scalability
- Better fault tolerance
- Horizontal scaling support

---

# 12. Development Trade-offs

Redis and Docker integration were simplified into Python asyncio queues to reduce setup complexity and accelerate prototype development.

This trade-off enabled faster development while still demonstrating event-driven asynchronous workflows.

---

# 13. Future Improvements

- Kafka integration
- RabbitMQ integration
- Distributed worker nodes
- Persistent memory layer
- Monitoring and observability
- Authentication support
- Kubernetes deployment

---

# 14. Conclusion

This project successfully demonstrates a scalable Agentic AI orchestration system capable of handling complex multi-step tasks using asynchronous execution, specialized AI agents, streaming responses, retry handling, queue-based communication, and manual batching.
