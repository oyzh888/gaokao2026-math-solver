# GaokaoMath-2026 · P19 — Benchmark Methodology

一个**单题、深度**的 LLM 数学推理小型 benchmark：拿 2026 年中国高考新高考 I 卷
最难的压轴题（第 19 题，17 分），让 16 个模型在同一道题上同台作答，逐题对照标准
答案评分，并对比「带 agentic 工具（Claude Code harness）」与「纯 API 单次调用」两种
设定的差异。

> ⚠️ 这是一个 **case study / probe**，不是统计意义上的大规模 benchmark。
> n = 1 道题、每模型 n = 1 次采样、单人工评委。结论的解读边界见文末「局限」。

---

## 1. 题目（the task）

**来源**：2026 新高考 I 卷数学第 19 题，全卷压轴，17 分。
被 11 省采用（浙江、山东、广东、福建、湖南、湖北、河北、江苏、江西、安徽、河南），
是考生规模最大的卷种。题型为「抽象函数 + 自定义集合 + 反证法」，一线教师评为
本卷最难、逼近全国卷历史难度峰值。

精确题面见 [`docs/problem_19_exact.md`](docs/problem_19_exact.md)（已对 PDF 扫描件
逐字核对）。核心：

> 函数 $f$ 定义域 $\mathbb{R}$，$x<0$ 时 $f(x)=2^x$；定义
> $D(x_0)=\{d : f(x_0+d)>f(x_0)\}$。
> (1) 若 $x\ge0$ 时 $f(x)=1-x$，求 $D(-1)$；
> (2) $f$ 奇函数、$f(x_1)\le f(x_2)$、$x_1x_2\ne0$ ⟹ $D(x_2)\subseteq D(x_1)$；
> (3) 给定两条抽象性质，(i) 证 $f(0)\ge1$；(ii) 证 $f$ 在 $(0,+\infty)$ 递增。

**标准答案**（扫描件解析）：(1) $D(-1)=(0,\tfrac32)$；(2)(3) 见解析页。
其中 **(3)(ii) 是公认难点**，扫描件标答本身在最后一步也以「可构造……」概述。

### 题目真实性核验（为什么可信）

- **年份/卷别/题号/题型**：多个考后（2026-06-08）独立来源交叉确认 —— 中国教育在线
  官方真题页、知乎个人解答、CSDN/新浪真题解析、B站讲解视频，均指向「2026 全国一卷
  / 新高考 I 卷 T19 压轴，抽象函数 + 新定义 + 集合 + 反证法」。
- **精确数字**（底数 2、$D(-1)$、答案 $(0,\tfrac32)$）：由作者**亲自比对真题扫描件
  原图**（`paper/gk100_pages/page_11.png`、`page_12.png`，来源页标题《2026新高考全国
  一卷数学真题及答案解析（完整版）》）逐字确认。
- **免责**：试卷为考后网络整理版（高考100 等教育门户），非教育部官方发布。仅供学习
  研究，不含任何受版权保护的教辅内容。

---

## 2. 输入协议（the prompt）— 保证 fair

**喂给所有模型的 input 是同一段纯题面**，见 [`prompts/problem_19.txt`](prompts/problem_19.txt)。

关键纪律——**输入里没有任何泄漏**：

- ❌ 不含标准答案
- ❌ 不含解题提示、引理、方向引导
- ❌ 不含「这题很难 / 注意第三问」之类的元信息暗示
- ✅ 只有题面本身 + 通用指令（「严格证明 / 分小问 / 不要联网 / 不要用工具」）

> 这条很重要：任何提示都会污染结论。我们刻意让所有模型从零开始。

---

## 3. 两种设定（the conditions）

| 组 | 设定 | 是否可用工具 |
|----|------|--------------|
| 🛠️ **Harness** | 把题目交给 **Claude Code**（agentic harness） | ✅ 可写并执行代码、数值实验、自我验证 |
| 🌐 **API** | 各厂商**官方 API 单次调用** | ❌ prompt 明确要求「不要用工具」 |
| 🕰️ **Legacy** | 同 API 组，但用**两年前的老模型** | ❌ 同上 |

> **这是一个有意的对照变量，不是不公平。** 我们就是想量化「同一个底座模型
> （如 Claude Opus / Sonnet），套上能写代码自验证的 harness 后，在最难一步上能
> 不能走得更远」。结论见 §6。

---

## 4. 模型清单与来源

> 作者实际是在一个**企业模型网关**（Azure OpenAI / Amazon Bedrock / Google Vertex AI）
> 上跑的，所以 `solutions/` 里的原始输出来自该网关。`runners/` 下提供了**等价的、
> 用各厂商公开 API 的可复现脚本**——同一 prompt、同一模型族，配好自己的 key 即可复跑。

| 组 | 模型 | 厂商 / 调用方式 |
|----|------|------------------|
| Harness | Claude Opus 4.8 (harness) | Anthropic via Claude Code |
| Harness | Claude Sonnet 4.6 (harness) | Anthropic via Claude Code |
| API | GPT-5.5 | OpenAI |
| API | GPT-5 | OpenAI |
| API | Gemini 2.5 Pro / 3.1 Pro / 3.5 Flash / 3.1 Flash-Lite | Google |
| API | Claude Haiku 4.5 / Opus 4.8 / Sonnet 4.6（纯 API） | Anthropic |
| Legacy | GPT-5 mini | OpenAI |
| Legacy | Gemini 2.5 Flash-Lite | Google |
| Legacy | Claude 3.5 Haiku (2024-10) | Anthropic |
| Legacy | Claude 3 Sonnet (2024-02) | Anthropic |
| Legacy | Claude 3 Haiku (2024-03) | Anthropic |

所有原始解答（逐字）见 [`solutions/problem_19/model_runs/`](solutions/problem_19/model_runs/)。
harness 组的**模型自写工作脚本**（数值验证用）见同目录 `scripts/`——这是 harness 确实
用了工具的证据。

---

## 5. 评分标准（the rubric）

逐题对照扫描件标准答案，每个小问 (1)(2)(3i)(3ii) 给一个符号：

| 符号 | 含义 |
|------|------|
| ✅ | 完整、严格、结论正确 |
| 🟡 | 结论对但有跳步 / 末步不严 |
| ❌ | 结论错或基本没做出来 |
| — | 未产出（超时等） |

- **(3)(ii) 从宽**：因为它是公认难点、连标答都概述，所以只要抓住「引理 P / 平移
  构造矛盾」的正确骨架即给 ✅，细节缺失给 🟡。
- 综合档：四问全 ✅ = 满分级 🥇；接近 = 🥈。

完整评分表见 [`solutions/problem_19/compare.html`](solutions/problem_19/compare.html)
（也已上线：见 README 的 Demo 链接）。

---

## 6. 主要发现（the findings）

1. **最难一步 (3ii) 是分水岭**。(1)(2)(3i) 几乎所有当代模型都能做对；真正拉开差距
   的是 (3ii) 的「把负半轴已知信息灌进未知正半轴」的反证构造。

2. **Harness 帮在了刀刃上**。同样是 Claude Opus / Sonnet：
   - **纯 API**：在 (3ii) 卡住（Opus 写出探索式草稿但未收尾；Sonnet 自陈「没找到
     矛盾」）。
   - **套 Claude Code harness**：两个都做到满分级。Opus 版做了 ~200 万随机点数值
     实验，归纳失败模式逆推出「禁带引理」，再写成证明——**工具让它在最难一步走得
     更远**。这正面验证了「agentic harness 对最难子问题有实质帮助」。

3. **纯 API 第一梯队**：GPT-5.5、Gemini 2.5 Pro、Gemini 3.5 Flash 单次调用即满分级。

4. **两年代际进步肉眼可见**：2024 年的 Claude 3 系列**连第 (1) 问都算错**
   （给成 $(-\infty,-1)$ / $(-1,2)$ / $\{d<0\}$），而今天的同级小模型
   （Haiku 4.5、Gemini Flash、GPT-5 mini）能稳定做对 (1) 并在 (3) 上走对方向。

---

## 7. 局限（honest caveats）

这个 benchmark 是 **solid 的演示**，但**不是统计意义的排名**。读结论时请记住：

1. **单题、单样本**：n = 1 道题，每模型只跑 1 次。模型有随机性，重跑（尤其 3ii）
   可能波动。**不要据此对模型做强排序。**
2. **人工单评委评分**：✅/🟡/❌ 由作者（借助 Claude）逐题对照标答给出，未做多评委
   /盲评/多次平均。3ii 的「从宽」判定带主观性。
3. **harness vs API 非同等条件**：harness 组可用工具，API 组被禁止——这是**有意的
   对照变量**，对比的是「设定」而非「裸模型能力」。
4. **网关 vs 公开 API 可能有细微差异**：原始输出跑在企业网关上；`runners/` 的公开
   API 版本是等价复现，但厂商在不同接入点的版本/默认参数可能略有不同。

欢迎用 `runners/` 复跑、增加题目、做多次采样、引入第二评委——见 README 的「如何贡献」。
