# 🎓 GaokaoMath-2026 · 压轴题多模型 Benchmark

> 拿 **2026 年中国高考新高考 I 卷数学最难的压轴题**（第 19 题，17 分），
> 让 **16 个大模型同台作答**，逐题对照标准答案评分，并对比
> 「带 agentic 工具的 Claude Code harness」与「纯 API 单次调用」两种设定的差异。

[![demo](https://img.shields.io/badge/live-demo-5ec8ff)](https://gaokao.steveouyang.com)
&nbsp;一道题，16 个模型，3 种设定，完整可复现。

🔗 **在线对比页**：https://gaokao.steveouyang.com/compare.html
（评分榜 + 每个模型的逐字解答 + 动画讲解）

---

## TL;DR

- 这道题的 **(1)(2)(3i)** 当代模型基本都能做；真正的分水岭是 **(3)(ii)** ——
  一个「把负半轴已知信息灌进未知正半轴」的反证构造，连标准答案都只能概述。
- **同一个 Claude（Opus/Sonnet），纯 API 在 (3ii) 卡住；套上 Claude Code harness
  后两个都做到满分级** —— Opus 版跑了 ~200 万随机点数值实验逆推出关键引理。
  **工具帮在了刀刃上。**
- 纯 API 第一梯队：GPT-5.5 / Gemini 2.5 Pro / Gemini 3.5 Flash 单次调用即满分级。
- 2024 年的 Claude 3 系列**连第 (1) 问都算错** —— 两年代际进步肉眼可见。

完整方法论、来源核验、评分标准、**诚实的局限说明**见 **[BENCHMARK.md](BENCHMARK.md)**。

---

## 这道题

> 函数 $f$ 定义域 $\mathbb{R}$，当 $x<0$ 时 $f(x)=2^x$；对任意 $x_0$ 定义集合
> $$D(x_0)=\{\,d\in\mathbb{R} : f(x_0+d)>f(x_0)\,\}.$$
> **(1)** 若 $x\ge0$ 时 $f(x)=1-x$，求 $D(-1)$；
> **(2)** 若 $f$ 是奇函数、$f(x_1)\le f(x_2)$、$x_1x_2\ne0$，证明 $D(x_2)\subseteq D(x_1)$；
> **(3)** 设 $f$ 满足 ① $f(x_1)\le f(x_2)\Rightarrow D(x_2)\subseteq D(x_1)$；② $0<x<1$ 时 $f(x)<f(0)$。
> &nbsp;&nbsp;(i) 证 $f(0)\ge1$；(ii) 证 $f$ 在 $(0,+\infty)$ 单调递增。

精确题面（已对扫描件逐字核对）：[`docs/problem_19_exact.md`](docs/problem_19_exact.md)。
试卷原件（12 页含解析）：[`paper/`](paper/)。

---

## 结果速览

| 组 | 模型 | (1) | (2) | (3i) | (3ii) | 综合 |
|----|------|:---:|:---:|:---:|:---:|------|
| 🛠️ Harness | Claude Opus 4.8 (harness) | ✅ | ✅ | ✅ | ✅ | 🥇 满分级 |
| 🛠️ Harness | Claude Sonnet 4.6 (harness) | ✅ | ✅ | ✅ | ✅ | 🥇 满分级 |
| 🌐 API | GPT-5.5 | ✅ | ✅ | ✅ | ✅ | 🥇 满分级 |
| 🌐 API | Gemini 2.5 Pro | ✅ | ✅ | ✅ | ✅ | 🥇 满分级 |
| 🌐 API | Gemini 3.5 Flash | ✅ | ✅ | ✅ | ✅ | 🥇 满分级 |
| 🌐 API | GPT-5 | ✅ | ✅ | ✅ | 🟡 | 🥈 接近 |
| 🌐 API | Gemini 3.1 Pro | ✅ | ✅ | ✅ | 🟡 | 🥈 接近 |
| 🌐 API | Claude Haiku 4.5 | ✅ | ✅ | ✅ | 🟡 | 🥈 接近 |
| 🌐 API | Gemini 3.1 Flash-Lite | ✅ | 🟡 | 🟡 | 🟡 | 思路对 |
| 🌐 API | Claude Opus 4.8（纯 API） | ✅ | 🟡 | 🟡 | 🟡 | 思路对 |
| 🌐 API | Claude Sonnet 4.6（纯 API） | ✅ | 🟡 | 🟡 | ❌ | 部分 |
| 🕰️ Legacy | GPT-5 mini | ✅ | 🟡 | ✅ | 🟡 | 接近 |
| 🕰️ Legacy | Gemini 2.5 Flash-Lite | ✅ | 🟡 | 🟡 | 🟡 | 思路对 |
| 🕰️ Legacy | Claude 3.5 Haiku (2024-10) | ❌ | 🟡 | 🟡 | 🟡 | 偏弱 |
| 🕰️ Legacy | Claude 3 Sonnet (2024-02) | ❌ | 🟡 | ❌ | ❌ | 偏弱 |
| 🕰️ Legacy | Claude 3 Haiku (2024-03) | ❌ | ❌ | ❌ | ❌ | 做不动 |

✅ 完整严格 · 🟡 结论对但跳步 · ❌ 错或缺。评分标准 + 边界见 [BENCHMARK.md](BENCHMARK.md)。

---

## 仓库结构

```
gaokao2026-math-solver/
├── README.md                  # 你在这
├── BENCHMARK.md               # ⭐ 方法论 / 来源核验 / 评分标准 / 局限
├── HOWTO_USE.md               # ⭐ 以后怎么用它辅助做题
├── prompts/
│   ├── problem_19.txt         # 喂给所有模型的纯题面输入（无任何提示）
│   └── problem_19_short.txt   # 精简版 prompt
├── runners/                   # 公开 API 的可复现 runner（OpenAI/Anthropic/Gemini）
│   ├── run_openai.py
│   ├── run_anthropic.py
│   └── run_gemini.py
├── docs/
│   └── problem_19_exact.md    # 精确题面（对扫描件核对）
├── paper/                     # 试卷原件：PDF + 逐页 PNG
├── scripts/
│   └── build_compare.py       # 把各模型解答 + 评分编译成 compare.html
└── solutions/problem_19/
    ├── index.html             # 标准解答页
    ├── explainer.html         # 动画讲解页
    ├── compare.html           # 多模型对比页（评分榜 + 全部解答）
    └── model_runs/            # 16 个模型的逐字原始输出
        ├── <model>.md
        └── scripts/           # harness 模型自写的数值验证脚本（工具使用证据）
```

---

## 快速复现

```bash
pip install openai anthropic google-genai

export OPENAI_API_KEY=sk-...      # 或 ANTHROPIC_API_KEY / GEMINI_API_KEY

# 让某个模型从零解这道题（输入只有题面，无任何提示）
python runners/run_openai.py    prompts/problem_19.txt gpt-5.5           > my_run.md
python runners/run_anthropic.py prompts/problem_19.txt claude-opus-4-5   > my_run.md
python runners/run_gemini.py    prompts/problem_19.txt gemini-2.5-pro    > my_run.md

# 重新编译对比页
python scripts/build_compare.py
```

> 原始结果跑在企业模型网关上；`runners/` 是等价的公开 API 版本。详见
> [`runners/README.md`](runners/README.md) 与 [BENCHMARK.md §4](BENCHMARK.md)。

---

## 方法 & 来源（出处都写清楚）

| 环节 | 用了什么 | 出处 |
|------|----------|------|
| 试卷获取 | 考后网络整理版（高考100 等门户）PDF + 逐页 PNG | `paper/` |
| 题面 OCR | Gemini-3.1-pro vision 转录扫描页 → LaTeX | `docs/problem_19_exact.md` |
| 题目核验 | 多源交叉 + 作者人工比对扫描件原图 | [BENCHMARK.md §1](BENCHMARK.md) |
| 模型调用 | OpenAI / Anthropic / Google 官方 SDK | `runners/` |
| Harness 组 | **Claude Code**（agentic，可写代码自验证） | `solutions/.../model_runs/scripts/` |
| 评分 | 人工逐题对照扫描件标答（单评委，3ii 从宽） | [BENCHMARK.md §5](BENCHMARK.md) |
| 展示 | 纯静态 HTML + MathJax，部署到 Cloudflare Pages | `solutions/problem_19/*.html` |

---

## ⚠️ 诚实声明（务必先读）

这是一个**单题深度 case study**，不是统计排名：
- **n = 1 题、每模型 1 次采样、单人工评委** —— 不要据此对模型做强排序。
- **harness vs API 是有意的对照变量**（一个可用工具、一个不可），对比的是「设定」。
- 试卷为**网络整理版**（非官方），仅供学习研究。

详细局限与解读边界见 [BENCHMARK.md §7](BENCHMARK.md)。

---

## License & 致谢

- 代码 MIT。试卷/题目版权归原权利人，本仓库仅汇总公开网络资源与自动求解过程，
  **不含任何受版权保护的教辅内容**，仅供学习研究。
- 🤖 Generated & solved with [Claude Code](https://claude.com/claude-code).
