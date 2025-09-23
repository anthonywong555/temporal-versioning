# NDE Auto Restart

This project illustrate how auto restart a workflow when it runs into a Nondeterminism error.

## Setup & Demo

To run this example, you will need to do the following:

```sh
uv sync
```

After that, you want to have three different terminal windows open in this directory to run the following commands:

```sh
temporal server start-dev
```

```sh
uv run watchfiles --filter python "python worker.py"
```

```sh
uv run python starter.py
```

## How this works

where the failure_reason = "NonDeterminismError"