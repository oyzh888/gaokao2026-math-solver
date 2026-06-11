# Model Runners

每个 runner 读取一个 prompt 文件（纯题面，**无任何提示/答案**），调用对应厂商的 API，把模型的完整解答打到 stdout。

```bash
python runners/run_openai.py   prompts/problem_19.txt gpt-5.5            > out.md
python runners/run_anthropic.py prompts/problem_19.txt claude-opus-4-5  > out.md
python runners/run_gemini.py   prompts/problem_19.txt gemini-2.5-pro    > out.md
```

## 认证

这些 runner 使用各厂商的**官方公开 SDK + 标准环境变量**：

| Runner | SDK | 需要的环境变量 |
|--------|-----|----------------|
| `run_openai.py` | `openai` | `OPENAI_API_KEY` |
| `run_anthropic.py` | `anthropic` | `ANTHROPIC_API_KEY` |
| `run_gemini.py` | `google-genai` | `GEMINI_API_KEY` |

```bash
pip install openai anthropic google-genai
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GEMINI_API_KEY=...
```

> **关于本仓库里 `solutions/` 的原始输出**：它们是作者在一个内部模型网关
> （企业版 Azure OpenAI / Amazon Bedrock / Vertex AI）上跑出来的，
> 因此原始脚本走的是内部认证路径。这里提供的 runner 是**等价的、用公开 API
> 的可复现版本**——同样的 prompt、同样的模型族，任何人配好自己的 key 即可复跑。
> 模型族与厂商对应见 [`../BENCHMARK.md`](../BENCHMARK.md)。
