from agents.base_agent import BaseAgent
import asyncio

class WriterAgent(BaseAgent):

    async def run(self, task):

        await asyncio.sleep(2)

        return {
            "report":
            """
AI Investment Report

1. Healthcare AI startups are rapidly growing.
2. Enterprise AI adoption is increasing.
3. Generative AI market expanding quickly.

Recommendation:
Focus on healthcare and enterprise AI sectors.
            """
        }