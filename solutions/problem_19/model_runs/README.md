# 原始模型输出（raw LLM outputs）

这里是 16 个模型对第 19 题的**逐字原始解答**，未经任何编辑——用于 sanity check：
你可以自己读每个模型到底写了什么、对照 [`../../../BENCHMARK.md`](../../../BENCHMARK.md)
里的人工评分是否合理。

- **输入**：所有模型喂的都是同一段纯题面 [`PROMPT.txt`](PROMPT.txt)（无任何提示/答案）。
  精简版见 [`PROMPT_SHORT.txt`](PROMPT_SHORT.txt)。
- **`scripts/`**：harness 组模型（Claude Code）**自己写的数值验证脚本**——是「harness
  确实用了工具」的证据（如 `p3ii_robust.py` 用 200 万随机点验证条件①）。

## 文件 → 模型 → 评分对照

| 文件 | 组 | 模型 | (1)(2)(3i)(3ii) |
|------|----|------|------------------|
| `harness_opus.md` | 🛠️ harness | Claude Opus 4.8 (Claude Code) | ✅✅✅✅ 🥇 |
| `harness_sonnet.md` | 🛠️ harness | Claude Sonnet 4.6 (Claude Code) | ✅✅✅✅ 🥇 |
| `azure_gpt-5.5.md` | 🌐 api | GPT-5.5 | ✅✅✅✅ 🥇 |
| `gemini_gemini-2.5-pro.md` | 🌐 api | Gemini 2.5 Pro | ✅✅✅✅ 🥇 |
| `gemini_gemini-3.5-flash.md` | 🌐 api | Gemini 3.5 Flash | ✅✅✅✅ 🥇 |
| `azure_gpt-5.md` | 🌐 api | GPT-5 | ✅✅✅🟡 🥈 |
| `gemini_gemini-3.1-pro-preview.md` | 🌐 api | Gemini 3.1 Pro | ✅✅✅🟡 🥈 |
| `claude_haiku.md` | 🌐 api | Claude Haiku 4.5 | ✅✅✅🟡 🥈 |
| `gemini_gemini-3.1-flash-lite.md` | 🌐 api | Gemini 3.1 Flash-Lite | ✅🟡🟡🟡 |
| `bedrock_opus.md` | 🌐 api | Claude Opus 4.8（纯 API） | ✅🟡🟡🟡 |
| `bedrock_sonnet.md` | 🌐 api | Claude Sonnet 4.6（纯 API） | ✅🟡🟡❌ |
| `azure_gpt-5-mini.md` | 🕰️ legacy | GPT-5 mini | ✅🟡✅🟡 |
| `gemini_gemini-2.5-flash-lite.md` | 🕰️ legacy | Gemini 2.5 Flash-Lite | ✅🟡🟡🟡 |
| `bedrock_claude35_haiku.md` | 🕰️ legacy | Claude 3.5 Haiku (2024-10) | ❌🟡🟡🟡 |
| `bedrock_claude3_sonnet.md` | 🕰️ legacy | Claude 3 Sonnet (2024-02) | ❌🟡❌❌ |
| `bedrock_claude3_haiku.md` | 🕰️ legacy | Claude 3 Haiku (2024-03) | ❌❌❌❌ |

✅ 完整严格 · 🟡 结论对但跳步 · ❌ 错或缺。标答：(1) $D(-1)=(0,\tfrac32)$；
(3i) $f(0)\ge1$；(3ii) $f$ 在 $(0,+\infty)$ 递增。

> 注：文件名里的 `azure_`/`bedrock_`/`gemini_` 前缀只反映作者当时用的内部网关入口
> （Azure OpenAI / Amazon Bedrock / Vertex AI），模型本身是对应厂商的标准模型。
> 公开 API 的等价复现脚本见 [`../../../runners/`](../../../runners/)。
