# System Design Document

## Architecture Overview

This project implements a scalable Agentic AI orchestration system capable of handling complex multi-step tasks using specialized AI agents coordinated through asynchronous workflows.

The system accepts user requests, decomposes them into subtasks, assigns them to specialized agents, coordinates execution asynchronously, and streams responses back to the user in real time.

The architecture is designed with scalability, modularity, asynchronous execution, fault tolerance, and streaming communication in mind.

---

# System Architecture

User Request
      ↓
FastAPI API Layer
      ↓
Workflow Orchestrator
      ↓
Planner Agent
      ↓
┌──────────────┬──────────────┐
↓              ↓              ↓
Retriever   Analyzer      Writer
Agent        Agent         Agent
      ↓
Streaming/WebSocket Response

---

# Components

## 1. API Layer

The API layer is implemented using FastAPI.

Responsibilities:
- Accept user requests
- Trigger workflow execution
- Return responses
- Handle WebSocket connections
- Stream progressive outputs

---

## 2. Workflow Engine

The Workflow Engine coordinates execution between all agents.

Responsibilities:
- Manage orchestration logic
- Coordinate asynchronous execution
- Aggregate agent outputs
- Handle workflow sequencing

Implementation uses:

```python
asyncio.gather()
for concurrent execution of agents.

3. Planner Agent

The Planner Agent decomposes complex tasks into smaller executable subtasks.

Responsibilities:

Understand user intent
Break tasks into subtasks
Assign subtasks to specialized agents

Example:

subtasks = [
    {"agent": "retriever"},
    {"agent": "analyzer"},
    {"agent": "writer"}
]
4. Retriever Agent

The Retriever Agent gathers contextual information required for processing.

Responsibilities:

Simulate information retrieval
Prepare contextual inputs
Provide data to downstream agents
5. Analyzer Agent

The Analyzer Agent processes and analyzes retrieved information.

Responsibilities:

Analyze collected information
Generate insights
Process intermediate outputs
6. Writer Agent

The Writer Agent generates the final structured response.

Responsibilities:

Aggregate outputs
Generate final report
Produce user-facing responses
Async Orchestration

The system uses asynchronous execution for scalability and concurrency.

Implementation:

await asyncio.gather(
    retrieved_task,
    analyzed_task
)

Benefits:

Concurrent task execution
Reduced latency
Improved scalability
Efficient resource utilization
Streaming Responses

WebSocket-based streaming is implemented to provide real-time updates while execution continues.

Example streamed messages:

Planning tasks...
Retriever Agent completed
Analyzer Agent completed
Writer Agent completed
Final report generated

Benefits:

Real-time progress tracking
Improved user experience
Progressive execution visibility
Queue-Based Communication

The architecture uses asynchronous queue-based communication implemented using Python asyncio queues.

Responsibilities:

Event-driven communication
Decoupled execution
Task coordination
Scalable workflow management
Retry Mechanism

Retry handling is implemented for fault tolerance.

Implementation features:

Automatic retries
Configurable retry count
Delay between retry attempts

Benefits:

Improved reliability
Increased resilience
Better fault tolerance
Manual Batching

Custom batching logic is implemented independently using a BatchProcessor.

Responsibilities:

Group tasks together
Process batches efficiently
Improve throughput

Benefits:

Reduced overhead
Improved scalability
Better resource utilization
Scalability Considerations

The system was designed with scalability in mind.

Implemented scalability features:

Asynchronous execution
Concurrent agent processing
Queue-based communication
Streaming responses
Retry handling
Manual batching
Decoupled architecture
Scaling Issue Encountered

Managing multiple concurrent WebSocket streaming connections while coordinating asynchronous agent execution increased event-loop overhead during development.

As the number of active streaming clients increased, synchronization and resource management became more challenging.

Design Decision to Improve

Future versions would replace local asyncio queues with distributed message brokers such as Kafka or RabbitMQ.

Advantages:

Persistent messaging
Distributed scalability
Better fault tolerance
Horizontal scaling support
Development Trade-offs

Redis and Docker integration were simplified into Python asyncio queues to reduce environment setup complexity and accelerate prototype development.

This trade-off enabled faster implementation while still demonstrating event-driven asynchronous workflows.

Future Improvements
Kafka integration
RabbitMQ integration
Distributed worker nodes
Persistent memory layer
Advanced monitoring
Authentication support
Production deployment
Kubernetes orchestration
Conclusion

This project successfully demonstrates a scalable Agentic AI orchestration system capable of handling complex multi-step tasks using asynchronous workflows, streaming responses, retry handling, queue-based communication, and specialized AI agents.
