from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):

    async def run(self, task):

        subtasks = [
            {
                "agent": "retriever",
                "task": "Collect information"
            },
            {
                "agent": "analyzer",
                "task": "Analyze data"
            },
            {
                "agent": "writer",
                "task": "Generate final report"
            }
        ]

        return subtasks