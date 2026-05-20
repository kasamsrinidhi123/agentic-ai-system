import asyncio

async def retry_operation(agent, task, retries=3):

    for attempt in range(retries):

        try:

            return await agent.run(task)

        except Exception as e:

            print(f"Retry {attempt + 1} failed")

            if attempt == retries - 1:
                raise e

            await asyncio.sleep(2)