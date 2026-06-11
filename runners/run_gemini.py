#!/usr/bin/env python3
"""Run a Google Gemini model on a prompt file. Public-API, reproducible version.

Usage:
    GEMINI_API_KEY=... python runners/run_gemini.py prompts/problem_19.txt gemini-2.5-pro

The prompt file must contain ONLY the problem statement (no hints, no answer).
Uses the public Gemini Developer API (https://ai.google.dev) via google-genai.
"""
import sys, os
from google import genai

def main():
    if len(sys.argv) < 3:
        sys.exit("usage: run_gemini.py <prompt_file> <model>")
    prompt = open(sys.argv[1], encoding="utf-8").read()
    model = sys.argv[2]

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    r = client.models.generate_content(model=model, contents=prompt)
    print(r.text)

if __name__ == "__main__":
    main()
