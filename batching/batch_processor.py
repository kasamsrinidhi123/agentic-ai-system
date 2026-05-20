class BatchProcessor:

    def __init__(self, batch_size=3):

        self.tasks = []

        self.batch_size = batch_size

    async def add_task(self, task):

        self.tasks.append(task)

        if len(self.tasks) >= self.batch_size:

            return await self.process_batch()

    async def process_batch(self):

        batch = self.tasks[:]

        self.tasks.clear()

        results = []

        for task in batch:

            results.append(
                f"Processed: {task}"
            )

        return results