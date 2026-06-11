#!/usr/bin/env python3
"""Run an Anthropic Claude model on a prompt file. Public-API, reproducible version.

Usage:
    ANTHROPIC_API_KEY=sk-ant-... python runners/run_anthropic.py prompts/problem_19.txt claude-opus-4-5

The prompt file must contain ONLY the problem statement (no hints, no answer).

NOTE: This is the *pure-API* runner (single call, no tools) — the "API group"
in the benchmark. The "harness group" results were produced by running the
problem through Claude Code (an agentic harness with code-execution tools);
that is a different setup, documented in ../BENCHMARK.md.
"""
import sys
import anthropic

def main():
    if len(sys.argv) < 3:
        sys.exit("usage: run_anthropic.py <prompt_file> <model>")
    prompt = open(sys.argv[1], encoding="utf-8").read()
    model = sys.argv[2]

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    r = client.messages.create(
        model=model,
        max_tokens=20000,
        messages=[{"role": "user", "content": prompt}],
    )
    print("".join(b.text for b in r.content if b.type == "text"))
    print(f"<!-- usage: in={r.usage.input_tokens} out={r.usage.output_tokens} -->", file=sys.stderr)

if __name__ == "__main__":
    main()
