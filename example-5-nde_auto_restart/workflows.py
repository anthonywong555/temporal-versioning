import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import SendEmailInput, send_email


@workflow.defn(failure_exception_types=[workflow.NondeterminismError])
class SleepForDaysWorkflow:
    def __init__(self) -> None:
        self.is_complete = False

    @workflow.run
    async def run(self) -> str:
        while not self.is_complete:
            await workflow.execute_activity(
                send_email,
                SendEmailInput("30 days until the next email"),
                start_to_close_timeout=timedelta(seconds=10),
            )
            # Run the workflow first then 
            # uncomment this line of code
            #await workflow.execute_activity(
            #    send_email,
            #    SendEmailInput("30 days until the next email"),
            #    start_to_close_timeout=timedelta(seconds=10),
            #)
            await workflow.wait(
                [
                    asyncio.create_task(workflow.sleep(timedelta(minutes=1))),
                    asyncio.create_task(
                        workflow.wait_condition(lambda: self.is_complete)
                    ),
                ],
                return_when=asyncio.FIRST_COMPLETED,
            )
        return "done!"

    @workflow.signal
    def complete(self):
        self.is_complete = True