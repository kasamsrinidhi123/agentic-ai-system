from fastapi import FastAPI, WebSocket

from orchestrator.workflow import WorkflowEngine

from streaming.websocket_manager import ConnectionManager

import asyncio

app = FastAPI()

workflow = WorkflowEngine()

manager = ConnectionManager()


@app.get("/")
async def home():

    return {
        "message": "Agentic AI System Running"
    }


@app.post("/execute")
async def execute(task: dict):

    result = await workflow.execute(task)

    return result


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        await manager.send_message(
            "Planning tasks..."
        )

        await asyncio.sleep(1)

        await manager.send_message(
            "Retriever Agent completed"
        )

        await asyncio.sleep(1)

        await manager.send_message(
            "Analyzer Agent completed"
        )

        await asyncio.sleep(1)

        await manager.send_message(
            "Writer Agent completed"
        )

        await asyncio.sleep(1)

        await manager.send_message(
            "Final report generated"
        )

    except Exception as e:

        print(e)

    finally:

        await manager.disconnect(websocket)