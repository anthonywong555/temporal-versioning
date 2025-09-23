import asyncio
import uuid
from typing import Optional

from temporalio.client import Client
from temporalio.common import RetryPolicy
from __init__ import TASK_QUEUE
from workflows import SleepForDaysWorkflow

async def main(client: Optional[Client] = None):
    client = client or await Client.connect("localhost:7233")
    await client.start_workflow(
        SleepForDaysWorkflow.run,
        id=f"sleep-for-days-workflow-id-{uuid.uuid4()}",
        task_queue=TASK_QUEUE,
        retry_policy=RetryPolicy(
            non_retryable_error_types=["NondeterminismError"],
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
