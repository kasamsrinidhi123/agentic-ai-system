from agents.base_agent import BaseAgent
import asyncio

class RetrieverAgent(BaseAgent):

    async def run(self, task):

        await asyncio.sleep(2)

        return {
            "retrieved_data":
            [
                "OpenAI funding increased",
                "Healthcare AI startups growing",
                "Enterprise AI demand rising"
            ]
        }