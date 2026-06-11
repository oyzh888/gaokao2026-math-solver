#!/usr/bin/env python3
"""Run an OpenAI model on a prompt file. Public-API, reproducible version.

Usage:
    OPENAI_API_KEY=sk-... python runners/run_openai.py prompts/problem_19.txt gpt-5.5

The prompt file must contain ONLY the problem statement (no hints, no answer).
Output (the model's full solution) goes to stdout; token usage to stderr.
"""
import sys, os
from openai import OpenAI

def main():
    if len(sys.argv) < 3:
        sys.exit("usage: run_openai.py <prompt_file> <model> [reasoning_effort]")
    prompt = open(sys.argv[1], encoding="utf-8").read()
    model = sys.argv[2]
    effort = sys.argv[3] if len(sys.argv) > 3 else "medium"

    client = OpenAI()  # reads OPENAI_API_KEY
    kw = dict(model=model,
              messages=[{"role": "user", "content": prompt}],
              max_completion_tokens=100000)
    # reasoning models (gpt-5*, o*) accept reasoning_effort; chat models ignore it
    try:
        r = client.chat.completions.create(reasoning_effort=effort, **kw)
    except Exception:
        r = client.chat.completions.create(**kw)

    print(r.choices[0].message.content or "[EMPTY]")
    try:
        u = r.usage
        rt = getattr(getattr(u, "completion_tokens_details", None), "reasoning_tokens", "?")
        print(f"<!-- usage: reasoning={rt} total={u.completion_tokens} -->", file=sys.stderr)
    except Exception:
        pass

if __name__ == "__main__":
    main()
