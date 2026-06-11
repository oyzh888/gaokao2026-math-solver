# 解题过程

## 第(1)小问

**已知：** $x < 0$ 时 $f(x) = 2^x$；$x \geq 0$ 时 $f(x) = 1-x$。求 $D(-1)$。

$D(-1) = \{d \in \mathbb{R} : f(-1+d) > f(-1)\}$

计算 $f(-1) = 2^{-1} = \dfrac{1}{2}$

故需求满足 $f(-1+d) > \dfrac{1}{2}$ 的所有 $d$。

**令 $t = -1+d$，即分情况讨论 $t$ 的范围：**

**情况1：** $t < 0$，即 $-1+d < 0$，即 $d < 1$。

此时 $f(t) = 2^t > \dfrac{1}{2} = 2^{-1}$，故 $t > -1$，即 $d > 0$。

结合 $d < 1$，得 $0 < d < 1$。

**情况2：** $t \geq 0$，即 $d \geq 1$。

此时 $f(t) = 1-t > \dfrac{1}{2}$，故 $t < \dfrac{1}{2}$，即 $0 \leq t < \dfrac{1}{2}$，即 $1 \leq d < \dfrac{3}{2}$。

综合两种情况：$D(-1) = \left(0, \dfrac{3}{2}\right)$。

$$\boxed{D(-1) = \left(0,\ \dfrac{3}{2}\right)}$$

---

## 第(2)小问

**已知：** $f(x)$ 是奇函数，$f(x_1) \leq f(x_2)$，$x_1 x_2 \neq 0$。证明 $D(x_2) \subseteq D(x_1)$。

**证明：**

任取 $d \in D(x_2)$，即 $f(x_2 + d) > f(x_2)$。

需证 $d \in D(x_1)$，即 $f(x_1 + d) > f(x_1)$。

**关键引理：** 利用 $x < 0$ 时 $f(x) = 2^x$（严格递增）以及 $f$ 是奇函数，先研究 $f$ 的性质。

由 $f$ 是奇函数：$f(-x) = -f(x)$，且 $f(0) = 0$。

对 $x < 0$：$f(x) = 2^x \in (0,1)$；

对 $x > 0$：$f(x) = -f(-x) = -2^{-x} \in (-1, 0)$（因为 $-x < 0$）。

故 $f$ 在 $(-\infty, 0)$ 上严格递增（值域 $(0,1)$），在 $(0,+\infty)$ 上严格递增（值域 $(-1,0)$）。

**注意** $f(x) < 0$ 对 $x > 0$，$f(0) = 0$，$f(x) > 0$ 对 $x < 0$。

因此对任意 $x$，$f$ 在 $\mathbb{R}$ 上严格递增（跨越零点时：$x_1 < 0 < x_2 \Rightarrow f(x_1) > 0 > f(x_2)$，矛盾，所以只需注意同侧单调性与整体单调性）。

实际验证整体单调性：设 $a < b$。
- 若 $a < b < 0$：$f(a) = 2^a < 2^b = f(b)$。✓
- 若 $a < 0 = b$：$f(a) = 2^a > 0 = f(0)$？不对！$2^a < 1$，但 $f(a) = 2^a > 0 = f(0)$，故 $f$ 在 $a < 0 < b$ 时 $f(a) > 0 > f(b)$，**不是整体单调递增**。

重新整理：$f$ 在 $\mathbb{R}$ 上**不是**单调的（负数处 $f > 0$，正数处 $f < 0$）。

**重新思路**：直接利用 $D$ 的集合性质。

**核心观察：** 对任意 $x_0$，分析 $D(x_0)$ 的结构。

设 $x_0 < 0$：$f(x_0) = 2^{x_0}$。

$D(x_0) = \{d : f(x_0+d) > 2^{x_0}\}$

- 若 $x_0 + d < 0$：$2^{x_0+d} > 2^{x_0} \Rightarrow d > 0$；且需 $x_0+d < 0$ 即 $d < -x_0$。给出 $d \in (0, -x_0)$。
- 若 $x_0 + d \geq 0$：$f(x_0+d) = -2^{-(x_0+d)}$（由奇函数，$f(x) = -2^{-x}$ 对 $x>0$，$f(0)=0$）。

  需 $-2^{-(x_0+d)} > 2^{x_0}$，即 $-2^{-(x_0+d)} > 2^{x_0} > 0$，左边为负右边为正，不可能。

  若 $x_0+d = 0$：$f(0) = 0 > 2^{x_0}$？$2^{x_0} > 0$，故不成立。

所以当 $x_0 < 0$ 时，$D(x_0) = (0, -x_0)$。

设 $x_0 > 0$：$f(x_0) = -2^{-x_0} < 0$。

$D(x_0) = \{d: f(x_0+d) > -2^{-x_0}\}$

- 若 $x_0+d < 0$（即 $d < -x_0 < 0$）：$f(x_0+d) = 2^{x_0+d} > 0 > -2^{-x_0}$，故所有 $d < -x_0$ 均满足。
- 若 $x_0+d = 0$：$f(0) = 0 > -2^{-x_0}$，满足。即 $d = -x_0$ 满足。
- 若 $x_0+d > 0$（即 $d > -x_0$）：$-2^{-(x_0+d)} > -2^{-x_0} \Rightarrow 2^{-(x_0+d)} < 2^{-x_0} \Rightarrow -(x_0+d) < -x_0 \Rightarrow d > 0$。

  结合 $d > -x_0 > -x_0$（已有），此时条件为 $d > 0$（当 $d > -x_0$ 时，若 $x_0 > 0$ 则 $-x_0 < 0$，故 $d > -x_0$ 包含 $d > 0$ 和 $-x_0 < d \leq 0$）。

  更仔细：$d > -x_0$ 且 $x_0 + d > 0$ 已满足。条件 $d > 0$：
  - $d \in (-x_0, 0]$：$f(x_0+d) = -2^{-(x_0+d)}$，需 $> -2^{-x_0}$，即 $2^{-(x_0+d)} < 2^{-x_0}$，即 $d > 0$，不满足（$d \leq 0$）。

    当 $d = 0$：$f(x_0) = -2^{-x_0}$，不严格大于，不满足。
    当 $-x_0 < d < 0$：$x_0 + d \in (0, x_0)$，$f(x_0+d) = -2^{-(x_0+d)} \in (-2^{-x_0+x_0-d}, ...)$，需 $-2^{-(x_0+d)} > -2^{-x_0}$，即 $2^{-(x_0+d)} < 2^{-x_0}$，即 $x_0+d > x_0$，即 $d > 0$，不满足。

  - $d > 0$（且 $d > -x_0$ 自动满足因为 $-x_0 < 0 < d$）：满足。

综合 $x_0 > 0$ 时：$D(x_0) = (-\infty, -x_0) \cup \{-x_0\} \cup (0, +\infty) = (-\infty, -x_0] \cup (0, +\infty)$。

**现在证明 $D(x_2) \subseteq D(x_1)$，已知 $f(x_1) \leq f(x_2)$，$x_1 x_2 \neq 0$。**

由上面的分析，$f(x) = 2^x$（$x<0$）取值 $(0,1)$，$f(0)=0$，$f(x) = -2^{-x}$（$x>0$）取值 $(-1,0)$。

$f(x_1) \leq f(x_2)$ 意味着什么？分情况：

**情况A：** $x_1 < 0, x_2 < 0$。

$2^{x_1} \leq 2^{x_2} \Rightarrow x_1 \leq x_2$，故 $-x_1 \geq -x_2 > 0$。

$D(x_2) = (0, -x_2)$，$D(x_1) = (0, -x_1)$。

由 $-x_1 \geq -x_2$，故 $(0,-x_2) \subseteq (0,-x_1)$，即 $D(x_2) \subseteq D(x_1)$。✓

**情况B：** $x_1 > 0, x_2 > 0$。

$-2^{-x_1} \leq -2^{-x_2} \Rightarrow 2^{-x_1} \geq 2^{-x_2} \Rightarrow x_1 \leq x_2$，故 $-x_1 \geq -x_2$（即 $-x_1$ 更大，但都是负数）。

实际上 $-x_1 \leq -x_2 < 0$（因为 $x_1 \leq x_2$ 给出 $-x_1 \geq -x_2$）。

等等，$x_1 \leq x_2 > 0$ 意味着 $-x_1 \geq -x_2$，即 $-x_2 \leq -x_1 < 0$。

$D(x_1) = (-\infty, -x_1] \cup (0,+\infty)$，$D(x_2) = (-\infty, -x_2] \cup (0,+\infty)$。

由 $-x_2 \leq -x_1$，故 $(-\infty, -x_2] \subseteq (-\infty, -x_1]$，从而 $D(x_2) \subseteq D(x_1)$。✓

**情况C：** $x_1 < 0, x_2 > 0$。

$f(x_1) = 2^{x_1} > 0$，$f(x_2) = -2^{-x_2} < 0$。

$f(x_1) \leq f(x_2)$ 即 $2^{x_1} \leq -2^{-x_2} < 0$，矛盾（左边正，右边负）。**此情况不存在。**

**情况D：** $x_1 > 0, x_2 < 0$。

$f(x_1) = -2^{-x_1} < 0$，$f(x_2) = 2^{x_2} > 0$。

$f(x_1) \leq f(x_2)$ 自然成立（负数 $\leq$ 正数）。

$D(x_1) = (-\infty, -x_1] \cup (0,+\infty)$（$-x_1 < 0$），$D(x_2) = (0, -x_2)$（$-x_2 > 0$）。

需证 $(0,-x_2) \subseteq (-\infty,-x_1] \cup (0,+\infty)$。

$(0,-x_2) \subset (0,+\infty) \subseteq D(x_1)$。✓

**综上，四种情况均证毕。** $\blacksquare$

$$\boxed{D(x_2) \subseteq D(x_1) \text{ 已证}}$$

---

## 第(3)小问

**已知条件：**
① 若 $f(x_1) \leq f(x_2)$，则 $D(x_2) \subseteq D(x_1)$；
② 当 $0 < x < 1$ 时，$f(x) < f(0)$。

### (3)(i) 证明 $f(0) \geq 1$

**证明：**

取 $x_0 = -1$（$x_0 < 0$），则 $f(-1) = 2^{-1} = \dfrac{1}{2}$。

**计算 $D(-1)$：**

$D(-1) = \{d: f(-1+d) > f(-1) = \tfrac{1}{2}\}$

分情况（利用 $x<0$ 时 $f(x)=2^x$，$f$ 在其他区间的值暂未知）：

- 若 $-1+d < 0$（即 $d < 1$）：$f(-1+d) = 2^{-1+d} > \tfrac{1}{2} = 2^{-1}$，故 $d > 0$，得 $d \in (0,1)$。
- 若 $-1+d \geq 0$（即 $d \geq 1$）：需 $f(-1+d) > \tfrac{1}{2}$，此时 $-1+d \geq 0$，$f$ 的值由其他定义确定，暂记为未知，但我们只需要知道 $D(-1) \supseteq (0,1)$（至少包含 $(0,1)$）。

实际上，$(0,1) \subseteq D(-1)$（由第一种情况已确定）。

**利用条件②：** 当 $0 < x < 1$ 时，$f(x) < f(0)$，即 $f(0) > f(x)$ 对 $x \in (0,1)$。

等价地，$f(x) \leq f(0)$（严格小于，故也有 $\leq$）对 $0 < x < 1$。

由条件①，$f(x) \leq f(0)$ 蕴含 $D(0) \subseteq D(x)$，对任意 $x \in (0,1)$。

**取 $x \in (0,1)$（$x_1 = x, x_2 = 0$，$f(x_1) \leq f(x_2) = f(0)$）：**

由条件①：$D(0) \subseteq D(x)$，对所有 $x \in (0,1)$。

**计算 $D(x)$ 对 $x \in (0,1)$：**

$D(x) = \{d: f(x+d) > f(x)\}$

取 $d = -x$（即 $x + d = 0$）：需判断 $f(0) > f(x)$，由条件②这是成立的，故 $-x \in D(x)$。

这给出 $-x \in D(x)$ 对所有 $x \in (0,1)$。

由 $D(0) \subseteq D(x)$，且 $-x \in D(x)$……这个方向似乎没直接用。

**换一个角度：**

我们已知 $d = \frac{1}{2} \in (0,1) \subseteq D(-1)$（因为 $-1 + \frac{1}{2} = -\frac{1}{2} < 0$，$f(-\frac{1}{2}) = 2^{-1/2} = \frac{1}{\sqrt{2}} > \frac{1}{2}$，确实在 $D(-1)$）。

**利用条件①与 $D(-1)$ 的关系：**

取 $x_0 = 0$：$D(0) = \{d: f(d) > f(0)\}$。

条件②说：$0 < d < 1 \Rightarrow f(d) < f(0)$，即 $(0,1) \cap D(0) = \emptyset$，换言之 $(0,1) \not\subseteq D(0)$。

**对比：** $D(-1) \supseteq (0,1)$（已证）。

若 $f(0) < \frac{1}{2} = f(-1)$，则 $f(0) \leq f(-1)$，由条件①：$D(-1) \subseteq D(0)$。

但 $(0,1) \subseteq D(-1) \subseteq D(0)$，而 $D(0) \cap (0,1) = \emptyset$，矛盾！

若 $f(0) = \frac{1}{2}$（即 $f(0) = f(-1)$），同样由条件①（$f(-1) \leq f(0)$ 即 $f(0) \leq f(-1)$，双向）：$D(-1) \subseteq D(0)$，同样得矛盾。

实际上只需 $f(0) \leq f(-1) = \frac{1}{2}$，就能推出 $D(-1) \subseteq D(0)$（由条件①，$x_1 = 0, x_2 = -1$，$f(0) \leq f(-1)$ 给出 $D(-1) \subseteq D(0)$）。

这与 $D(0) \cap (0,1) = \emptyset$ 矛盾（因为 $(0,1) \subseteq D(-1) \subseteq D(0)$）。

**故必须 $f(0) > f(-1) = \frac{1}{2}$，但我们需要证 $f(0) \geq 1$。**

需要更强的论证。

**更精细的计算：**

对任意 $n \in \mathbb{Z}^+$，考虑 $x_0 = -n$，$f(-n) = 2^{-n}$。

$D(-n) = \{d: f(-n+d) > 2^{-n}\}$

- 若 $-n+d < 0$（即 $d < n$）：$2^{-n+d} > 2^{-n}$，故 $d > 0$，得 $d \in (0, n)$。

故 $(0, n) \subseteq D(-n)$（至少）。

若 $f(0) < 1$，取 $n$ 大使得 $f(0) \leq f(-n) = 2^{-n}$... 但 $f(0) < 1$ 且 $2^{-n} \to 0$，所以对大 $n$，$f(0) > 2^{-n}$，即 $f(-n) \leq f(0)$... 

**重新整理：**

假设 $f(0) < 1$。

取 $a \in (f(0), 1)$（这样的 $a$ 存在），令 $-n = \log_2 a$（即取 $x_0 = \log_2 a < 0$）。

更直接地：令 $x_0 = \log_2(f(0)) < 0$（若 $f(0) \in (0,1)$，此时 $x_0 < 0$）。

则 $f(x_0) = 2^{x_0} = f(0)$，故 $f(x_0) \leq f(0)$（等号），由条件①：$D(0) \subseteq D(x_0)$。

**计算 $D(x_0)$（$x_0 < 0$）：**

$(0, -x_0) \subseteq D(x_0)$（由前面分析，因为对 $d \in (0,-x_0)$，$-x_0+d < 0$... 

等等，这里 $-x_0 = -\log_2(f(0)) > 0$（若 $f(0) < 1$）。

更仔细：$x_0 = \log_2(f(0)) < 0$（假设 $f(0) \in (0,1)$），$-x_0 = -\log_2(f(0)) = \log_2(\frac{1}{f(0)}) > 0$。

$D(x_0)$ 包含 $(0, -x_0)$（由前面负数点处 $D$ 的计算）。

但**关键问题**：$D(x_0)$ 中 $d \in (0, -x_0)$ 时 $x_0 + d \in (x_0, 0)$，均为负数，$f(x_0+d) = 2^{x_0+d} > 2^{x_0} = f(0)$。

所以 $D(x_0) \supseteq (0, -x_0) = (0, \log_2(\frac{1}{f(0)}))$。

由 $D(0) \subseteq D(x_0)$，我们得 $D(0) \subseteq D(x_0)$，即 $D(0) \subseteq \{d: f(x_0+d) > f(0)\}$... 这没有直接矛盾。

**让我换一个方向：**

直接利用 $D(0)$ 与已知条件。

条件②：$0 < x < 1 \Rightarrow f(x) < f(0)$，故 $0 \notin D(x)$... 不是。

条件②等价于：对 $x \in (0,1)$，$f(x) < f(0)$。

**取 $x_2 = 0, x_1 \in (0,1)$：** $f(x_1) < f(x_2) = f(0)$，即 $f(x_1) \leq f(x_2)$（严格小，当然 $\leq$）。由条件①，$D(0) \subseteq D(x_1)$，对所有 $x_1 \in (0,1)$。

**现在，$D(0) \subseteq D(x_1)$ 对所有 $x_1 \in (0,1)$。**

**$D(0) = \{d: f(d) > f(0)\}$。**

由条件②，$f(d) < f(0)$ 对 $d \in (0,1)$，故 $(0,1) \cap D(0) = \emptyset$。

若 $f(0) < 1$：取 $x_1 \in (0,1)$ 充分接近 $0$，$x_1 + d_0$...

**我尝试用"负轴"的信息：**

$f(-1) = \frac{1}{2}$。

$D(0) = \{d: f(d) > f(0)\}$。

注意 $d = -1 < 0$：$f(d) = f(-1) = \frac{1}{2}$。若 $f(0) < \frac{1}{2}$，则 $f(-1) > f(0)$，故 $-1 \in D(0)$。

更一般地，$f(d) = 2^d$ 对 $d < 0$，随 $d \to -\infty$ 趋于 $0$，随 $d \to 0^-$ 趋于 $1$。

若 $f(0) < 1$：存在 $\delta < 0$ 使 $2^\delta > f(0)$（取 $\delta$ 接近 $0$），即 $\delta \in D(0)$。

具体，若 $f(0) < 1$，取 $\delta = \log_2(f(0))$（若 $f(0) > 0$）或对 $f(0) \leq 0$ 则任意 $\delta < 0$ 均有 $f(\delta) = 2^\delta > 0 \geq f(0)$，故 $\delta \in D(0)$。

现在，假设 $f(0) < 1$，则 $(-\log_2 f(0), 0) \cdot (-1) \cdot ...$

重新更清晰：

**假设 $f(0) < 1$（欲推矛盾）。**

分两个子情况：

**子情况(a)：$f(0) \leq 0$。**

对所有 $d < 0$，$f(d) = 2^d > 0 \geq f(0)$，故 $d \in D(0)$，即 $(-\infty, 0) \subseteq D(0)$。

由 $D(0) \subseteq D(x_1)$ 对所有 $x_1 \in (0,1)$（由条件①和②），故 $(-\infty, 0) \subseteq D(x_1)$。

即 $f(x_1 + d) > f(x_1)$ 对所有 $d < 0, x_1 \in (0,1)$。

取 $x_1 \in (0,1)$，$d = -x_1 \in (-1, 0) \subset (-\infty,0)$：$f(0) > f(x_1)$。

这与条件②（$f(x_1) < f(0)$）**一致**，没有矛盾。

取 $x_1 \in (0,1)$，$d = -2x_1 \in (-2,0)$：$f(x_1 - 2x_1) = f(-x_1) > f(x_1)$，即 $f(-x_1) > f(x_1)$，$-x_1 \in (-1,0)$，$f(-x_1) = 2^{-x_1} > f(x_1)$。

由 $D(0) \subseteq D(x_1)$，我们还知道 $D(0) \subseteq D(x_1)$ 对 $x_1 \in (0,1)$。

考虑 $x_1 \in (0,1)$，$d = 1 - x_1 \in (0,1)$（因为 $x_1 \in (0,1)$）。

$x_1 + d = 1$。若$1 \in D(0)$（即 $f(1) > f(0)$），则 $1 - x_1 \in D(x_1)$，即 $f(1) > f(x_1)$。

但这不直接用到 $f(0) < 1$ 的假设...

**更系统的方法：**

注意到 $f$ 在 $(-\infty, 0)$ 上的值完全已知。利用条件①, 我们可以"传递"集合包含关系。

**引理：** 若 $a < 0$，则 $D(a) \supseteq (0, -a)$（已证）。

**利用条件①的逆向：** 若 $D(x_2) \not\subseteq D(x_1)$，则 $f(x_1) > f(x_2)$（条件①的逆否：$D(x_2) \not\subseteq D(x_1) \Rightarrow f(x_1) > f(x_2)$）。

等价地，条件①的逆否为：若 $D(x_2) \not\subseteq D(x_1)$，则 $f(x_1) > f(x_2)$。

**利用此逆否：**

设 $f(0) < 1$。

取 $x_0 < 0$ 使 $f(x_0) = 2^{x_0} > f(0)$（只需 $x_0 > \log_2(f(0))$ 且 $x_0 < 0$，若 $f(0) < 1$ 这样的 $x_0$ 存在）。

（若 $f(0) \leq 0$，取任意 $x_0 < 0$ 即可；若 $0 < f(0) < 1$，取 $x_0 \in (\log_2 f(0), 0)$。）

此时 $f(x_0) > f(0)$，由条件①（$f(0) \leq f(x_0)$，令 $x_1 = 0, x_2 = x_0$）：$D(x_0) \subseteq D(0)$。

$D(x_0) \supseteq (0, -x_0)$（$-x_0 > 0$，且 $(0,-x_0) \subseteq D(x_0)$）。

故 $(0, -x_0) \subseteq D(x_0) \subseteq D(0)$，即 $(0,-x_0) \subseteq D(0)$。

但 $D(0) \cap (0,1) = \emptyset$（由条件②）。

若 $-x_0 > 1$（即 $x_0 < -1$）... 取 $x_0 \in (-1, 0)$，则$-x_0 \in (0,1)$，$(0,-x_0) \subseteq (0,1)$，但$(0,-x_0) \subseteq D(0)$ 与 $D(0) \cap (0,1) = \emptyset$ 矛盾！

（只要 $-x_0 \in (0,1)$，即 $x_0 \in (-1,0)$，就有矛盾。）

**整理：**

假设 $f(0) < 1$。

若 $f(0) \leq 0$：取 $x_0 = -\frac{1}{2} \in (-1,0)$，$f(x_0) = 2^{-1/2} > 0 \geq f(0)$，故 $f(0) \leq f(x_0)$。

若 $0 < f(0) < 1$：取 $x_0 \in (\log_2 f(0), 0) \cap (-1, 0)$（此集合非空，因为 $\log_2 f(0) < 0$ 且 $(-1,0)$ 包含 $\log_2 f(0)$ 与 $0$ 之间的点，若 $\log_2 f(0) > -1$ 即 $f(0) > \frac{1}{2}$，则取 $x_0 \in (\log_2 f(0), 0)$，若 $\log_2 f(0) \leq -1$ 即 $f(0) \leq \frac{1}{2}$，则取 $x_0 \in (-1, 0)$，此时 $2^{x_0} > 2^{-1} = \frac{1}{2} \geq f(0)$）。

无论如何，在假设 $f(0) < 1$ 下，存在 $x_0 \in (-1, 0)$ 使得 $f(0) \leq f(x_0) = 2^{x_0}$：

- 若 $f(0) \leq 0$：$f(x_0) = 2^{x_0} > 0 \geq f(0)$，取任意 $x_0 \in (-1,0)$。✓
- 若 $0 < f(0) < 1$：$f(0) < 1 = 2^0$，且 $2^{x_0}$ 在 $x_0 \in (-1,0)$ 时取值 $(\frac{1}{2}, 1)$。只要 $f(0) \in (0, 1)$，我们需要 $f(0) \leq 2^{x_0}$，即 $x_0 \geq \log_2 f(0)$。
  - 若 $f(0) \in (\frac{1}{2}, 1)$：$\log_2 f(0) \in (-1, 0)$，取 $x_0 \in (\log_2 f(0), 0) \subset (-1,0)$，得 $2^{x_0} > f(0)$。✓
  - 若 $f(0) \leq \frac{1}{2}$：$\log_2 f(0) \leq -1$，取任意 $x_0 \in (-1,0)$，$2^{x_0} > 2^{-1} = \frac{1}{2} \geq f(0)$。✓

故在所有子情况下，存在 $x_0 \in (-1,0)$ 使 $f(0) < f(x_0)$（严格），即 $f(0) \leq f(x_0)$（条件①需要 $\leq$）。

实际上严格 $f(0) < f(x_0)$，当然也有 $f(0) \leq f(x_0)$。

由条件①（$f(0) \leq f(x_0)$，即 $x_1 = 0, x_2 = x_0$）：$D(x_0) \subseteq D(0)$。

由 $x_0 \in (-1,0)$，$D(x_0) \supseteq (0, -x_0)$，其中 $-x_0 \in (0,1)$。

故 $(0, -x_0) \subseteq D(x_0) \subseteq D(0)$，即 $(0,-x_0) \subseteq D(0)$，与 $D(0) \cap (0,1) = \emptyset$ 矛盾（因为 $-x_0 \in (0,1)$，$(0,-x_0) \subset (0,1)$，$(0,-x_0) \neq \emptyset$）。

**矛盾！故假设 $f(0) < 1$ 不成立，即 $f(0) \geq 1$。** $\blacksquare$

$$\boxed{f(0) \geq 1 \text{ 已证}}$$

---

### (3)(ii) 证明 $f(x)$ 在 $(0,+\infty)$ 上单调递增

**证明：**

设 $0 < x_1 < x_2$，需证 $f(x_1) < f(x_2)$（严格递增）。

**步骤1：先证 $f(x_1) \leq f(x_2)$（即排除 $f(x_1) > f(x_2)$）。**

假设 $f(x_1) > f(x_2)$，即 $f(x_2) \leq f(x_1)$... 

等等，若 $f(x_2) \leq f(x_1)$（即 $f(x_1) \geq f(x_2)$），由条件①（$x_1' = x_2, x_2' = x_1$，$f(x_2') = f(x_1) \geq f(x_2) = f(x_1')$）：$D(x_1) \subseteq D(x_2)$。

我们需要找矛盾。

**步骤2：分析 $D(x_1)$ 和 $D(x_2)$。**

取 $d = -x_1 \in D(x_1)$ 当且仅当 $f(0) > f(x_1)$。

由 (i)，$f(0) \geq 1 > 0$。若 $f(x_1) < f(0)$，则 $-x_1 \in D(x_1)$。

但我们不知道 $f(x_1)$ 与 $f(0)$ 的关系（对 $x_1 \geq 1$，我们没有条件②的直接保证）。

**更好的策略：** 利用已知点（负半轴）。

对 $c < 0$，$D(c) \supseteq (0,-c)$。

由条件①，$f(c) \leq f(x_1)$（即 $x_1' = c, x_2' = x_1$）给出 $D(x_1) \subseteq D(c)$。

反过来，$f(x_1) \leq f(c)$ 给出 $D(c) \subseteq D(x_1)$。

**若 $f(x_1) > f(x_2)$：**

存在一些 $d$ 在 $D(x_2)$ 中但不在 $D(x_1)$ 中吗？

实际上假设 $f(x_1) \geq f(x_2)$（即 $f(x_2) \leq f(x_1)$），则 $D(x_1) \subseteq D(x_2)$（由条件①，$x_1' = x_2, x_2' = x_1$，条件为 $f(x_1') = f(x_2) \leq f(x_1) = f(x_2')$，故 $D(x_2') \subseteq D(x_1')$，即 $D(x_1) \subseteq D(x_2)$）。

嗯，我们要推矛盾，来自 $D(x_1) \subseteq D(x_2)$。

**关键方向：** 找 $d \in D(x_1)$ 但 $d \notin D(x_2)$。

考虑 $d = x_2 - x_1 > 0$（因为 $x_2 > x_1 > 0$）。

$d \in D(x_1)$ iff $f(x_2) > f(x_1)$，即 $f(x_1) < f(x_2)$。

但我们假设 $f(x_1) \geq f(x_2)$，故 $d \notin D(x_1)$。这没有帮助。

**换一种思路：利用负半轴。**

取 $c = -(x_2 - x_1) < 0$（$c < 0$，$-c = x_2 - x_1 > 0$）。

$D(c) \supseteq (0, x_2 - x_1)$（因为 $c < 0$，$-c = x_2-x_1$）。

设 $d = \frac{x_2-x_1}{2} \in (0, x_2-x_1)$，则 $d \in D(c)$。

若 $f(c) \leq f(x_1)$（即 $f(x_1) \geq f(c) = 2^c = 2^{-(x_2-x_1)}$），由条件①，$D(x_1) \subseteq D(c)$。这不直接有用。

若 $f(x_1) \leq f(c)$（即 $f(x_1) \leq 2^{-(x_2-x_1)} < 1 \leq f(0)$），由条件①，$D(c) \subseteq D(x_1)$，故 $(0, x_2-x_1) \subseteq D(x_1)$，即 $f(x_1+d) > f(x_1)$ 对 $d \in (0, x_2-x_1)$。取 $d = x_2-x_1$...不在开区间内。

**再换思路：直接论证。**

目标：证明 $0 < x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$。

**利用 $f(0) \geq 1$ 和负半轴信息：**

**引理：** $f$ 在 $(0, +\infty)$ 上无上界和... 

**直接证明：**

取任意 $0 < x_1 < x_2$。

考虑 $d_0 = x_1 \in (0, x_2)$。

$d_0 \in D(0)$ iff $f(x_1) > f(0)$。

由 (i) $f(0) \geq 1$，由条件②对 $x_1 \in (0,1)$：$f(x_1) < f(0)$，故 $x_1 \notin D(0)$ 若 $x_1 \in (0,1)$。

对 $x_1 \geq 1$，不能直接用条件②。

**尝试证明 $f(x) \geq f(0) \geq 1$ 对 $x \geq 1$：**

由条件②，$f(0) > f(x)$ 对 $x \in (0,1)$，即 $f(0)$ 是 $(0,1)$ 上 $f$ 的上界。

取 $x_2 = 1, x_1 \in (0,1)$：若 $f(1) \leq f(x_1) < f(0)$（假设），由条件①：$D(x_1) \subseteq D(1)$。

这没有立即矛盾。

**让我重新从定义出发，更系统地推导：**

**命题：** $f$ 在 $(0, +\infty)$ 上严格单调递增。

**反设：** 存在 $0 < a < b$ 使 $f(a) \geq f(b)$，即 $f(b) \leq f(a)$。

由条件①：$D(a) \subseteq D(b)$。

**计算 $D(b)$ 的限制：**

$D(b) = \{d: f(b+d) > f(b)\}$。

$D(a) = \{d: f(a+d) > f(a)\}$。

**利用负半轴：**

取 $c \in (-b, -a)$（此区间非空，因为 $-b < -a < 0$）。

$c < 0$，故 $f(c) = 2^c$。

考虑 $d = -a \in D(x_0 = 0)$ iff $f(0) > f(0)$，不。

让我取 $d = -a$：

$d \in D(a)$ iff $f(a + (-a)) = f(0) > f(a)$。

**若 $f(a) < f(0)$（即 $f(0) > f(a)$）：** $-a \in D(a)$，由 $D(a) \subseteq D(b)$，$-a \in D(b)$，即 $f(b-a) > f(b)$。

注意 $b - a \in (0, b)$，故 $b-a > 0$。

这给出：在 $0 < b-a < b$ 的情况下，$f(b-a) > f(b)$。即在 $b$ 之前有点的 $f$ 值更大。

**若 $f(a) \geq f(0)$：** 

由 (i)，$f(0) \geq 1$，故 $f(a) \geq 1$。

由条件②（$a \in (0,1)$ 时 $f(a) < f(0)$），若 $a \in (0,1)$，则 $f(a) < f(0)$，故此子情况（$f(a) \geq f(0)$）要求 $a \geq 1$。

**Case 1: $a \geq 1$（以及 $b > a \geq 1$）：**

考虑点 $-1 < 0$，$f(-1) = 2^{-1} = \frac{1}{2}$。

$D(-1) \supseteq (0, 1)$（已知）。

由条件①，$f(-1) = \frac{1}{2} \leq f(0) \leq f(a)$（假设 $f(a) \geq f(0) \geq 1 > \frac{1}{2}$），所以 $f(-1) \leq f(a)$，由条件①：$D(a) \subseteq D(-1)$。

这意味着任何 $d \in D(a)$ 也在 $D(-1)$ 中。

现取 $d = -a + \epsilon$ for small $\epsilon > 0$... 这比较复杂。

**更简洁的方法：**

**关键思路：** 取 $c < 0$ 使得 $f(c) = 2^c$ 恰好与 $f(a)$ 的关系可控。

若 $f(a) \geq f(0) \geq 1$：

$f(c) = 2^c < 1 \leq f(0) \leq f(a)$ 对所有 $c < 0$。

故 $f(c) \leq f(a)$ 对所有 $c < 0$，由条件①：$D(a) \subseteq D(c)$ 对所有 $c < 0$。

取 $c \in (-b+a, 0)$（此区间含 $0$ 的左邻域中的一段，$-b+a = -(b-a) < 0$，故区间非空）。

注意 $c \in (-(b-a), 0)$ 时，$-c \in (0, b-a)$，$(0,-c) \subseteq (0, b-a) \subseteq D(c)$... 

Hmm，$D(c) \supseteq (0,-c)$ 当 $c < 0$。取 $c \in (-(b-a), 0)$：$D(c) \supseteq (0, -c)$，$-c \in (0, b-a)$。

$D(a) \subseteq D(c)$，所以... 不对，方向反了，$D(a) \subseteq D(c)$ 意思是 $a$ 的集合更小。

我好像绕圈子了。让我尝试完全不同的思路。

---

**证明 $f$ 在 $(0,+\infty)$ 上严格单调递增的干净方法：**

**目标：** $0 < x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$。

**第一步：证明 $f(x_1) \leq f(x_2)$（即不存在 $f(x_1) > f(x_2)$）。**

反设 $f(x_1) > f(x_2)$，即 $f(x_2) < f(x_1)$，故 $f(x_2) \leq f(x_1)$。

由条件①：$D(x_1) \subseteq D(x_2)$。

考虑 $d^* = -x_1 < 0$。

$f(x_1 + d^*) = f(0) \geq 1$。

由 (i)，$f(0) \geq 1$，且 $f(x) = 2^x < 1$ 对 $x < 0$。

若 $f(0) > f(x_1)$：$d^* = -x_1 \in D(x_1)$（因为 $f(0) > f(x_1)$）。

由 $D(x_1) \subseteq D(x_2)$：$-x_1 \in D(x_2)$，即 $f(x_2 - x_1) > f(x_2)$。

$x_2 - x_1 \in (0, x_2)$，令 $a' = x_2 - x_1, b' = x_2$，则$0 < a' < b'$ 且 $f(a') > f(b')$，我们得到同样的情况（但"距离" $b' - a' = x_1 < x_2 - x_1 = b - a$... 不一定变小）。

这种方法需要归纳或极小性论证，较复杂。

若 $f(0) \leq f(x_1)$：

$f(0) \leq f(x_1)$，由条件①（$x_1' = 0, x_2' = x_1$）：$D(x_1) \subseteq D(0)$。

结合 $D(x_1) \subseteq D(x_2)$：$D(x_1) \subseteq D(0) \cap D(x_2)$。

对 $D(0)$：由条件②，$f(d) < f(0)$ 对 $d \in (0,1)$，故 $(0,1) \cap D(0) = \emptyset$。

对 $d < 0$，$f(d) = 2^d$。$f(d) > f(0)$ iff $2^d > f(0)$。

若 $f(0) \geq 1$（已证），$2^d < 1 \leq f(0)$ 对 $d < 0$，故 $D(0) \cap (-\infty, 0) = \emptyset$。

故 $D(0) \subseteq [1, +\infty)$（$d \geq 1$ 或 $d = 0$ 不在 $D(0)$ 中... $d = 0$：$f(0) > f(0)$，不对）。

更准确：$D(0) = \{d: f(d) > f(0)\}$。对 $d < 0$：$f(d) = 2^d < 1 \leq f(0)$，故 $d \notin D(0)$。对 $d \in [0,1)$：条件②（$d > 0$）和 $d = 0$ 给 $f(0) \not> f(0)$，故 $D(0) \cap [0,1) = \emptyset$。

故 $D(0) \subseteq [1, +\infty)$。

由 $D(x_1) \subseteq D(0)$：$D(x_1) \subseteq [1, +\infty)$。

现在考虑 $d = -x_2 < 0$（因为 $x_2 > 0$）：$d < 0 \notin [1,+\infty)$，故$d \notin D(x_1)$，即 $f(0) \leq f(x_1)$（$f(x_1 + (-x_2)) = f(x_1-x_2)$，$x_1 - x_2 < 0$ 所以 $f(x_1-x_2) = 2^{x_1-x_2}$，$2^{x_1-x_2} \leq f(x_1)$）。

于是 $2^{x_1-x_2} \leq f(x_1)$。

还有 $d = x_2 - x_1 > 0$：$d \in D(x_1)$ iff $f(x_2) > f(x_1)$。但我们假设 $f(x_2) < f(x_1)$，故 $d = x_2-x_1 \notin D(x_1)$。

由 $D(x_1) \subseteq [1,+\infty)$，若$x_2 - x_1 < 1$（即 $x_2 < x_1 + 1$），$d \notin [1,+\infty)$，所以即使 $d \notin D(x_1)$也是一致的。若$x_2 - x_1 \geq 1$，$d \in [1,+\infty)$，可能在 $D(x_1)$...

**这条思路比较繁琐，让我找更优雅的方法。**

---

**优雅方法：利用条件①的逆否传递。**

**Claim：** $f$ 在 $(0,+\infty)$ 上严格单调递增。

**证明：**

设 $0 < x_1 < x_2$，需证 $f(x_1) < f(x_2)$。

**Step 1：** 建立 $D(x_0)$ 的基本性质。

对 $x_0 > 0$，考虑 $d = -x_0$：$f(x_0 + (-x_0)) = f(0) \geq 1 > 0$。

若 $f(x_0) < f(0)$，则 $-x_0 \in D(x_0)$。

**Step 2：** 证明 $f(x_1) < f(0)$ 对所有 $x_1 > 0$... 等下，只有条件②对 $x_1 \in (0,1)$ 保证了这个，对 $x_1 \geq 1$ 不知道。

**Step 3：** 利用"传递"。

由条件②，$f$ 在 $(0,1)$ 上的值均 $< f(0)$。

设 $x_1 \in (0,1)$：$f(x_1) < f(0)$。

对 $x_2 \in (0,1)$ 的情况，需证 $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$。

反设存在 $0 < x_1 < x_2 < 1$ 使 $f(x_1) \geq f(x_2)$，即 $f(x_2) \leq f(x_1)$，由条件①：$D(x_1) \subseteq D(x_2)$。

$d = -x_1 \in (0,1)$ 范围之外（$-x_1 < 0$）。

$d = x_2 - x_1 \in (0, x_2) \subset (0,1)$，$d \in D(x_1)$ iff $f(x_2) > f(x_1)$，由假设不成立，故 $d \notin D(x_1)$，OK，一致。

取 $d = -x_1 + \epsilon$ for small $\epsilon$... 

**Let me try a direct approach using negative axis.**

对 $x_0 \in (0, 1)$，我想证 $f(x_0)$ 随 $x_0$ 严格递增。

考虑 $c = -x_0 < 0$，$D(c) \supseteq (0, x_0)$（因为 $-c = x_0$）。

由于 $f(c) = 2^{-x_0} < 1 \leq f(0)$（由(i)），$f(0) > f(c)$... 

先处理 $D(0)$ 与 $D(c)$ 的关系：

$f(c) = 2^c < 1 \leq f(0)$，故 $f(c) \leq f(0)$，由条件①（$x_1' = c, x_2' = 0$，$f(c) \leq f(0)$）：$D(0) \subseteq D(c)$。

反过来，我们知道 $D(c) \supseteq (0,-c)=(0,x_0)$。

**想法：** 如果 $d \in D(x_2)$ 则 $d+x_2-x_1 \in D(x_1)$？不对，集合平移不适用。

**最终思路（基于逆否）：**

反设存在 $0 < x_1 < x_2$ 使 $f(x_1) \geq f(x_2)$。

不妨设 $f(x_1) = \max\{f(x_1), f(x_2)\}$（如有更多点，取 $f$ 值最大的）。

换言之，$f(x_2) \leq f(x_1)$，由条件①：$D(x_1) \subseteq D(x_2)$。

**关键：** 取 $d = x_1 - x_2 < 0$（因为 $x_1 < x_2$）。

$d \in D(x_2)$: $f(x_2 + d) = f(x_1) > f(x_2)$（由 $f(x_1) \geq f(x_2)$...等等，$f(x_1) \geq f(x_2)$ 不严格 $>$，若 $f(x_1) = f(x_2)$ 则 $f(x_1) \not> f(x_2)$）。

若 $f(x_1) > f(x_2)$：$d = x_1 - x_2 \in D(x_2)$。

由 $D(x_1) \subseteq D(x_2)$：...这没有给出 $d \in D(x_1)$ 的信息（包含关系方向不对）。

若 $f(x_1) > f(x_2)$，条件①（$f(x_2) \leq f(x_1)$，$x_1' = x_2, x_2' = x_1$）给出 $D(x_1) \subseteq D(x_2)$。

取 $d' = x_2 - x_1 > 0$：$d' \in D(x_1)$ iff $f(x_2) > f(x_1)$，但 $f(x_1) > f(x_2)$，故 $d' \notin D(x_1)$，OK，没用。

$d' \in D(x_2)$ iff $f(x_2 + x_2 - x_1) = f(2x_2 - x_1) > f(x_2)$。

$D(x_1) \subseteq D(x_2)$，所以$D(x_1)$中的元素都在$D(x_2)$中。

Now take $d'' = -x_2 < 0$: $d'' \in D(x_1)$ iff $f(x_1 - x_2) > f(x_1)$, i.e., $f(x_1-x_2) > f(x_1)$. Since $x_1 - x_2 < 0$, $f(x_1-x_2) = 2^{x_1-x_2}$. Is $2^{x_1-x_2} > f(x_1)$?

We know $f(x_1) \geq f(x_2) > 0$ (assuming $f(x_2) > 0$... we don't know that). 

**Let me try a completely different approach using what we have.**

We know:
- $f(x) = 2^x$ for $x < 0$ (given)
- $f(0) \geq 1$ (proved in (i))
- Condition ①: $f(x_1) \leq f(x_2) \Rightarrow D(x_2) \subseteq D(x_1)$
- Condition ②: $0 < x < 1 \Rightarrow f(x) < f(0)$

**First, prove $f$ is increasing on $(0,1)$:**

Suppose $0 < x_1 < x_2 < 1$. Need to show $f(x_1) < f(x_2)$.

By condition ②, $f(x_1) < f(0)$ and $f(x_2) < f(0)$.

Suppose for contradiction $f(x_1) \geq f(x_2)$ (i.e., $f(x_2) \leq f(x_1)$).

By condition ①: $D(x_1) \subseteq D(x_2)$.

Take $c = -(x_2 - x_1)/2 < 0$ (just some negative number related to $x_1, x_2$). Actually, let me try $c = x_1 - x_2 \in (-1, 0)$ and $-c = x_2 - x_1 \in (0,1)$.

$D(c)$: for $c < 0$, $D(c) \supseteq (0, -c) = (0, x_2-x_1)$.

$f(c) = 2^c = 2^{x_1-x_2} < 1 \leq f(0)$, so $f(c) \leq f(0)$.

$f(x_2) \leq f(x_1) < f(0)$, so: is $f(c) \leq f(x_2)$ or $f(c) \geq f(x_2)$? We don't know.

**Trying to find a specific $d$ in $D(x_1)$ but not in $D(x_2)$:**

A $d$ is in $D(x_1)$ but not $D(x_2)$ iff $f(x_1+d) > f(x_1)$ and $f(x_2+d) \leq f(x_2)$.

If $D(x_1) \subseteq D(x_2)$ (consequence of $f(x_2) \leq f(x_1)$), there's no such $d$. So we need to derive a contradiction from "$D(x_1) \subseteq D(x_2)$ for all $0 < x_1 < x_2 < 1$ with $f(x_2) \leq f(x_1)$".

Actually maybe I should look at this from the perspective of a specific $d$.

**Take $d = -x_2 < 0$. Is $d \in D(x_1)$?**

$f(x_1 + d) = f(x_1 - x_2)$. Since $x_1 < x_2$, $x_1 - x_2 < 0$, so $f(x_1-x_2) = 2^{x_1-x_2}$.

$d \in D(x_1)$ iff $2^{x_1-x_2} > f(x_1)$.

Since $f(x_1) < f(0) \leq 1$ and $2^{x_1-x_2} > 0$, this might or might not hold.

If $D(x_1) \subseteq D(x_2)$ and $d = -x_2 \in D(x_1)$, then $-x_2 \in D(x_2)$, i.e., $f(0) > f(x_2)$. That's fine (we know $f(x_2) < f(0)$).

No contradiction yet.

**Take $d = -x_1 < 0$. $d \in D(x_1)$ iff $f(0) > f(x_1)$. Since $x_1 \in (0,1)$, by condition ②, $f(x_1) < f(0)$, so $-x_1 \in D(x_1)$.**

By $D(x_1) \subseteq D(x_2)$: $-x_1 \in D(x_2)$, i.e., $f(x_2 - x_1) > f(x_2)$.

$x_2 - x_1 \in (0, x_2) \subset (0,1)$. So we have $f(x_2 - x_1) > f(x_2)$ where $0 < x_2 - x_1 < x_2 < 1$.

Now apply the same argument to $x_2 - x_1$ and $x_2$:
- $0 < x_2 - x_1 < x_2 < 1$
- $f(x_2 - x_1) > f(x_2)$, i.e., $f(x_2) \leq f(x_2 - x_1)$
- By condition ①: $D(x_2-x_1) \subseteq D(x_2)$
- $d = -(x_2-x_1) \in D(x_2-x_1)$ iff $f(0) > f(x_2-x_1)$: YES (since $x_2-x_1 \in (0,1)$)
- So $-(x_2-x_1) \in D(x_2)$, i.e., $f(x_2-(x_2-x_1)) = f(x_1) > f(x_2)$.

So $f(x_1) > f(x_2)$. But we assumed $f(x_2) \leq f(x_1)$, i.e., $f(x_1) \geq f(x_2)$.

Wait, this says $f(x_1) > f(x_2)$, which is consistent with our assumption $f(x_1) > f(x_2)$. No contradiction yet.

Hmm. Let me think more carefully. The assumption was $f(x_1) \geq f(x_2)$. I've derived $f(x_2 - x_1) > f(x_2)$ and then $f(x_1) > f(x_2)$. The latter is slightly stronger (strict) than the assumption.

So actually from $f(x_1) \geq f(x_2)$ we got $f(x_1) > f(x_2)$. Now let's keep going.

We have $f(x_2 - x_1) > f(x_2)$ and $f(x_1) > f(x_2)$.

So both $x_2 - x_1$ and $x_1$ "beat" $x_2$.

**Now apply the argument again to the pair $(x_1, x_2 - x_1)$ (note: we only know that $f(x_1)$ and $f(x_2 - x_1)$ are both $> f(x_2)$, but what's their relative order?):**

From $f(x_2 - x_1) > f(x_2)$ and $D(x_1) \subseteq D(x_2)$:

Actually, we've been assuming $f(x_2) \leq f(x_1)$, i.e., $D(x_1) \subseteq D(x_2)$.

We found $f(x_2-x_1) > f(x_2)$ (from $d = -x_1 \in D(x_1) \subseteq D(x_2)$).

**But what is the relationship between $f(x_2-x_1)$ and $f(x_1)$?**

Consider:
- If $x_1 < x_2 - x_1$, i.e., $x_2 > 2x_1$: both $x_1, x_2-x_1 \in (0,1)$.
- If $x_1 = x_2 - x_1$, i.e., $x_2 = 2x_1$: $x_1 = x_2-x_1$.
- If $x_1 > x_2-x_1$, i.e., $x_2 < 2x_1$: both still in $(0,1)$ since $x_2 < 1$.

**Apply the argument to the pair $(x_2-x_1, x_1)$ (in some order):**

If $f(x_1) \geq f(x_2-x_1)$ (assuming this), by condition ①: $D(x_2-x_1) \subseteq D(x_1)$.

$d = -(x_2-x_1) \in D(x_2-x_1)$ (since $x_2-x_1 \in (0,1)$, $f(0) > f(x_2-x_1)$).

So $-(x_2-x_1) \in D(x_1)$, i.e., $f(x_1-(x_2-x_1)) = f(2x_1-x_2) > f(x_1)$.

If $x_2 < 2x_1$ (i.e., $2x_1-x_2 > 0$): $f(2x_1-x_2) > f(x_1)$ where $2x_1-x_2 \in (0, x_1) \subset (0,1)$.

If $x_2 > 2x_1$: $2x_1-x_2 < 0$, $f(2x_1-x_2) = 2^{2x_1-x_2} > f(x_1)$. Since $f(x_1) < f(0) \leq 1$ and $2^{2x_1-x_2} < 1 \leq f(0)$, this gives $2^{2x_1-x_2} > f(x_1)$, i.e., $f(x_1) < 2^{2x_1-x_2}$.

OK so in both cases we get a new inequality. But I'm not seeing the contradiction directly.

**Let me step back and try a cleaner approach.**

**CLEAN PROOF OF (3)(ii):**

**Lemma (A):** $D(0) \subseteq [1, +\infty)$.

*Proof:* 
- For $d < 0$: $f(d) = 2^d < 1 \leq f(0)$, so $d \notin D(0)$.
- For $d = 0$: $f(0) \not> f(0)$, so $0 \notin D(0)$.
- For $d \in (0,1)$: by condition ②, $f(d) < f(0)$, so $d \notin D(0)$.
- Hence $D(0) \subseteq [1, +\infty)$. $\square$

**Lemma (B):** For $x > 0$, $f(x) \leq f(0)$ (actually $f(x) < f(0)$ for $x \in (0,1)$ by condition ②, but we need something for all $x > 0$).

Hmm, we don't know $f(x)$ vs $f(0)$ for $x \geq 1$.

**Lemma (C):** For $x > 0$, $D(0) \subseteq D(x)$ if $f(x) \leq f(0)$.

This is condition ① directly.

**Let me try to prove that $D(0) \supseteq [1, +\infty)$ (i.e., $D(0) = [1,+\infty)$ or at least $[1,\infty) \subseteq D(0)
