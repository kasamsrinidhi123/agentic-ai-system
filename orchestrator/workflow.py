from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.writer_agent import WriterAgent

import asyncio

class WorkflowEngine:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()

    async def execute(self, user_task):

        print("Planning tasks...")

        subtasks = await self.planner.run(user_task)

        print("Running Retriever and Analyzer in parallel...")

        retrieved_task = self.retriever.run(subtasks[0])

        analyzed_task = self.analyzer.run(subtasks[1])

        retrieved, analyzed = await asyncio.gather(
            retrieved_task,
            analyzed_task
        )

        print("Running Writer Agent...")

        final = await self.writer.run({
            "retrieved": retrieved,
            "analysis": analyzed
        })

        return final