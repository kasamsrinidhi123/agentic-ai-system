from agents.base_agent import BaseAgent
import asyncio

class AnalyzerAgent(BaseAgent):

    async def run(self, task):

        await asyncio.sleep(2)

        return {
            "analysis":
            "Healthcare AI and enterprise AI show strong investment potential."
        }