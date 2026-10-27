# Human Review Queue

Rank evaluation cases using explicit severity and confidence rules.

**Status:** small, AI-assisted portfolio prototype. Synthetic fixtures only; no client data, live model, or production deployment. Python standard library only.

## Run

From this directory with Python 3.10 or newer:

```sh
python main.py
python main.py sample.json
python -m unittest -v
```

On macOS/Linux, use `python3` if `python` is unavailable. Edit a copy of `sample.json` to try a new case. Input is JSON; the CLI prints a JSON result. Required keys and field types are illustrated in the sample; malformed schemas raise errors rather than producing valid scores.

## How it works

Read `evaluate()` in `main.py`. It is the complete evaluation logic. The CLI loads a file and prints the returned dictionary/list. `example_output.json` is the actual result of running the supplied sample.

## Limitations

A deterministic triage heuristic; confidence is supplied rather than calibrated. Not an autonomous hiring, medical, or legal decision system.

Toy fixtures demonstrate behavior; they do not establish model quality or real-world accuracy. Human review is still required.

## Your next contribution

Add reviewer disposition and audit history; check whether the priority rule overloads the queue.

## Interview demo

1. Explain the problem in one sentence.
2. Run the supplied example and trace one result to its input.
3. Change one field and predict the result before running it.
4. Explain one test and one limitation.
5. Describe what you personally changed; distinguish the AI-assisted scaffold from your own work.

## Files

- `main.py`: evaluation logic and command-line entry point.
- `sample.json`: fictional input fixture.
- `example_output.json`: generated output.
- `test_main.py`: expected outcomes for normal and edge cases.
