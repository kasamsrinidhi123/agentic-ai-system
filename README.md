# agentic-ai-system
Scalable multi-agent AI orchestration system with async workflows, streaming responses, retry handling, and manual batching.
# Agentic AI System for Multi-Step Tasks

## Overview

This project implements a scalable Agentic AI System capable of handling complex multi-step tasks using multiple specialized AI agents coordinated through asynchronous workflows.

The system accepts complex user requests, decomposes them into smaller executable subtasks, assigns tasks to specialized agents, and streams progressive responses back to the user in real time.

The architecture is designed with scalability, modularity, asynchronous execution, and fault tolerance in mind.

---

# Features

* Multi-agent architecture
* Planner Agent for task decomposition
* Retriever Agent for information collection
* Analyzer Agent for data processing
* Writer Agent for final response generation
* Asynchronous orchestration using `asyncio`
* WebSocket-based streaming responses
* Event-driven task queue
* Retry handling mechanism
* Manual batching implementation
* Scalable and modular system design

---

# Architecture

```text id="jlwmz8"
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
```

---

# Agent Responsibilities

## Planner Agent

* Breaks complex tasks into smaller subtasks
* Assigns subtasks to specialized agents

## Retriever Agent

* Collects contextual information
* Simulates external retrieval workflows

## Analyzer Agent

* Processes and analyzes retrieved information
* Generates insights

## Writer Agent

* Produces the final structured response/report

---

# Async Orchestration

The system uses asynchronous execution with:

```python id="jlwm72"
asyncio.gather()
```

to enable concurrent execution of multiple agents efficiently.

---

# Streaming Responses

WebSocket-based streaming is implemented to provide real-time updates while the workflow is executing.

Example streamed messages:

```text id="8jlwmq"
Planning tasks...
Retriever Agent completed
Analyzer Agent completed
Writer Agent completed
Final report generated
```

---

# Retry Mechanism

Fault tolerance is implemented using retry handling logic that retries failed agent executions automatically.

---

# Manual Batching

Custom batching logic is implemented independently to process grouped tasks efficiently and improve scalability.

---

# Technologies Used

* Python
* FastAPI
* asyncio
* WebSockets
* Async Queues
* OpenAI API (optional)
* Redis-ready architecture

---

# Project Structure

```text id="jlwm19"
agentic-ai-system/
│
├── agents/
├── api/
├── orchestrator/
├── streaming/
├── batching/
├── retry/
├── queue/
├── docs/
│
├── README.md
├── requirements.txt
└── .env.example
```

---

# How to Run

## Install Dependencies

```bash id="jlwm0o"
pip install -r requirements.txt
```

## Start Server

```bash id="jlwmq1"
uvicorn api.main:app --reload
```

---

# API Testing

Open Swagger UI:

```text id="jlwmtt"
http://127.0.0.1:8000/docs
```

---

# WebSocket Streaming Test

Connect using:

```text id="jlwm53"
ws://127.0.0.1:8000/ws
```

---

# Example API Request

```json id="jlwm3m"
{
  "task": "Generate AI investment report"
}
```

---

# Example Response

```json id="jlwmcw"
{
  "report": "AI Investment Report..."
}
```

---

# Scalability Considerations

* Decoupled agent-based architecture
* Asynchronous concurrent execution
* Event-driven communication
* Retry handling for resilience
* Queue-based workflow design
* Manual batching for throughput optimization

---

# Scaling Issue Encountered

Managing concurrent streaming connections while coordinating multiple asynchronous agents increased event-loop overhead during development.

---

# Design Decision to Improve

Future versions would replace local async queues with Kafka or RabbitMQ for distributed scalability and persistent messaging.

---

# Development Trade-offs

Redis/Docker integration was simplified into Python async queues to reduce environment setup complexity and accelerate prototype development.

---

# Future Improvements

* Kafka integration
* Distributed worker nodes
* Persistent memory layer
* Advanced observability
* Production deployment support

---

# Author

Srinidhi Kasam
