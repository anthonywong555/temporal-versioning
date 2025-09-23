import asyncio
import logging

from temporalio.client import Client
from temporalio.worker import Worker

from __init__ import TASK_QUEUE
from activities import send_email
from workflows import SleepForDaysWorkflow

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[SleepForDaysWorkflow],
        activities=[send_email],
    )

    await worker.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())