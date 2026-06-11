# 2026 新高考 I 卷 数学 第 19 题（17 分）解答

> 求解者：Claude Opus 4.8（在 Claude Code harness 中，边推导边用 Python 数值验证关键断言）。
> 全程未联网，独立推导；所有"关键引理 / 集合刻画 / 反例排除"均有 Python 脚本佐证。

## 题目

函数 $f(x)$ 定义域为 $\mathbb{R}$，当 $x<0$ 时 $f(x)=2^x$。对任意 $x_0\in\mathbb{R}$，定义集合
$$D(x_0)=\{d\in\mathbb{R}: f(x_0+d)>f(x_0)\}.$$

- **(1)** 若 $x\ge0$ 时 $f(x)=1-x$，求 $D(-1)$；
- **(2)** 若 $f(x)$ 是奇函数，$f(x_1)\le f(x_2)$，且 $x_1x_2\ne0$，证明 $D(x_2)\subseteq D(x_1)$；
- **(3)** 设 $f$ 满足：① 若 $f(x_1)\le f(x_2)$ 则 $D(x_2)\subseteq D(x_1)$；② 当 $0<x<1$ 时 $f(x)<f(0)$。
  - **(i)** 证明 $f(0)\ge1$；
  - **(ii)** 证明 $f$ 在 $(0,+\infty)$ 单调递增。

一个有用的等价改写（贯穿全题）：
$$d\in D(x_0)\iff x_0+d\in\{t:f(t)>f(x_0)\},\qquad\text{即}\quad D(x_0)=-x_0+\{t:f(t)>f(x_0)\}.$$
也就是说 $D(x_0)$ 是 **超水平集** $\{t:f(t)>f(x_0)\}$ 平移 $-x_0$ 的结果。

并且条件①的**逆否形式**（全题主力工具，记作 (★)）：
$$\boxed{\;f(q+d)>f(q)\ \text{且}\ f(p+d)\le f(p)\ \Longrightarrow\ f(p)>f(q).\;}\tag{$\star$}$$
（即：若存在 $d\in D(q)\setminus D(p)$，则不可能 $f(p)\le f(q)$，故 $f(p)>f(q)$。）

---

## (1) 求 $D(-1)$

此处 $f(x)=2^x\ (x<0)$，$f(x)=1-x\ (x\ge0)$。$f(-1)=2^{-1}=\tfrac12$。

$d\in D(-1)\iff f(-1+d)>\tfrac12$。令 $t=-1+d$，分段解 $f(t)>\tfrac12$：

- $t<0$：$2^t>\tfrac12\iff t>-1$，结合 $t<0$ 得 $t\in(-1,0)$；
- $t\ge0$：$1-t>\tfrac12\iff t<\tfrac12$，结合 $t\ge0$ 得 $t\in[0,\tfrac12)$。

合并：$\{t:f(t)>\tfrac12\}=(-1,\tfrac12)$。再由 $d=t+1$ 平移得
$$\boxed{D(-1)=\left(0,\ \tfrac32\right).}$$
两端均**开**（$d=0$ 给 $f(-1)=f(-1)$ 不满足严格大于；$d=\tfrac32$ 给 $t=\tfrac12$，$f=\tfrac12$ 不满足）。

**数值验证（`p1.py`）**：在 $d\in[-5,5]$ 上以 $2.5\times10^{-5}$ 步长扫描 $f(-1+d)>\tfrac12$，得使其成立的 $d$ 范围 $\approx(0.00002,\ 1.49998)$，端点处 $f$ 恰等于 $\tfrac12$。与 $(0,\tfrac32)$ 完全吻合。

```
f(-1) = 0.5
d range where f(-1+d)>1/2: 2e-05 1.49998
d=0.0:    f=0.500 > 0.5? False     d=1.5:    f=0.500 > 0.5? False
d=0.0001: f=0.500 > 0.5? True      d=1.4999: f=0.500 > 0.5? True
```

---

## (2) $f$ 奇函数，$f(x_1)\le f(x_2)$，$x_1x_2\ne0$ ⟹ $D(x_2)\subseteq D(x_1)$

**$f$ 的显式结构。** $x<0$ 时 $f(x)=2^x\in(0,1)$，严格增；由奇性 $f(0)=0$，且 $x>0$ 时
$$f(x)=-f(-x)=-2^{-x}\in(-1,0),\quad\text{在 }(0,\infty)\text{ 上严格增}.$$
注意整体**并不单调**：$x<0$ 取正值 $(0,1)$，$x>0$ 取负值 $(-1,0)$。

**$D(x_0)$ 的显式刻画**（由超水平集平移）：

- 若 $x_0<0$（则 $f(x_0)=2^{x_0}\in(0,1)$）：只有负自变量 $t<0$ 才能取到 $>f(x_0)$ 的值，且 $2^t>2^{x_0}\iff t>x_0$，故 $\{t:f(t)>f(x_0)\}=(x_0,0)$，于是
$$D(x_0)=(0,\,-x_0).$$
- 若 $x_0>0$（则 $f(x_0)=-2^{-x_0}\in(-1,0)$）：所有 $t\le0$ 给的值 $\ge0>f(x_0)$（含 $f(0)=0$），所有 $t>x_0$ 给 $-2^{-t}>-2^{-x_0}$，故 $\{t:f(t)>f(x_0)\}=(-\infty,0]\cup(x_0,\infty)$，于是
$$D(x_0)=(-\infty,\,-x_0]\cup(0,\infty).$$

**按符号分类证明。** 因 $x_1x_2\ne0$，$x_i$ 非零；又 $f$ 在负区取正、正区取负：

- **情形 A（$x_1<0,x_2<0$）**：$f(x_1)\le f(x_2)\Rightarrow 2^{x_1}\le2^{x_2}\Rightarrow x_1\le x_2\Rightarrow -x_2\le -x_1$。
  $D(x_2)=(0,-x_2)\subseteq(0,-x_1)=D(x_1)$。✓
- **情形 B（$x_1>0,x_2>0$）**：$f(x_1)\le f(x_2)\Rightarrow -2^{-x_1}\le-2^{-x_2}\Rightarrow x_1\le x_2\Rightarrow -x_2\le-x_1$。
  $D(x_2)=(-\infty,-x_2]\cup(0,\infty)\subseteq(-\infty,-x_1]\cup(0,\infty)=D(x_1)$。✓
- **情形 C（$x_1<0,x_2>0$）**：$f(x_1)>0>f(x_2)$ 与 $f(x_1)\le f(x_2)$ 矛盾，前提空，无需讨论。
- **情形 D（$x_1>0,x_2<0$）**：$D(x_2)=(0,-x_2)\subseteq(0,\infty)\subseteq(-\infty,-x_1]\cup(0,\infty)=D(x_1)$。✓

四种情形全部成立，故 $D(x_2)\subseteq D(x_1)$。$\blacksquare$

**数值验证**：
- `p2.py`：直接定义奇函数 $f$，随机抽 $2\times10^5$ 组 $(x_1,x_2,d)$，凡满足 $f(x_1)\le f(x_2)$ 且 $d\in D(x_2)$ 者，检验 $d\in D(x_1)$ —— **0 个反例**。
- `p2c.py`：数值反解出各 $x_0$ 的 $D(x_0)$ 区间，完全符合上面的显式公式（例如 $x_0=-1\Rightarrow D=(0,1)$；$x_0=1\Rightarrow D=(-\infty,-1]\cup(0,\infty)$）。
- `p2e.py`：用显式公式版的 $D$ 再随机测 $5\times10^5$ 组，**0 个反例**。

---

## (3)(i) 证明 $f(0)\ge1$

**反证。** 设 $f(0)=c<1$。因 $2^x\to1\ (x\to0^-)$，可取
$$x=\log_2\frac{c+1}{2}\in(-1,0),\qquad 2^x=\frac{c+1}{2}\in(c,1).$$
于是 $f(0)=c<2^x=f(x)$，即 $f(0)\le f(x)$。由条件① $\Rightarrow D(x)\subseteq D(0)$。

- 一方面，对 $0<d<-x$，有 $x+d\in(x,0)\subset(-\infty,0)$，故 $f(x+d)=2^{x+d}>2^x=f(x)$，即 $d\in D(x)$。因此 $(0,-x)\subseteq D(x)\subseteq D(0)$。
- 另一方面，$-x\in(0,1)$，故 $(0,-x)\subset(0,1)$；由条件② 对一切 $d\in(0,1)$ 有 $f(d)<f(0)$，即 $d\notin D(0)$。所以 $(0,-x)\cap D(0)=\varnothing$。

非空区间 $(0,-x)$ 既 $\subseteq D(0)$ 又与 $D(0)$ 不交，矛盾。故 $f(0)\ge1$。$\blacksquare$

**数值验证（`p3i.py`）**：取 $c=0.9$，脚本给出 $x=\log_2(0.95)\approx-0.074\in(-1,0)$，$2^x=0.95\in(c,1)$，且 $-x\in(0,1)$，反证构造的各项条件逐一核对成立。

---

## (3)(ii) 证明 $f$ 在 $(0,+\infty)$ 单调递增 —— **本题最难**

> 这一问我**先用 Python 大量数值实验**：随机/参数化构造函数，检测哪些能通过条件①②，从失败的反例里逆推出"应该成立的引理"，再回到严格证明。下面给出最终的严格链条，并标注每一步对应的数值实验。

### 关键引理（均仅由条件①②与 (i) 推出）

设 $x>0$。记条件① 的逆否形式 (★)。我们依次建立四条引理。

#### 引理 0（自相似 / 负点对约束 ♦）
对**任意** $a_1<a_2<0$，恒有 $f(a_1)=2^{a_1}<2^{a_2}=f(a_2)$，即 $f(a_1)\le f(a_2)$，由① 得 $D(a_2)\subseteq D(a_1)$。
令 $h=a_2-a_1>0$，$V=2^{a_2}\in(0,1)$，代入 $t=a_2+d$ 化简，得
$$\boxed{(\diamond)\quad \forall V\in(0,1),\ \forall h>0:\quad f(t)>V\ \Longrightarrow\ f(t-h)>V\cdot2^{-h}.}$$

#### 引理 1（禁带 BAND：$(0,1)$ 是正半轴的禁区）
**对一切 $x>0$，$f(x)\le0$ 或 $f(x)\ge1$；开区间 $(0,1)$ 不可能被取到。**

*证.* 反设某 $b>0$ 有 $f(b)\in(0,1)$。取 $a=\log_2 f(b)<0$，则 $f(a)=2^a=f(b)\le f(b)$，由① 得 $D(b)\subseteq D(a)$。
取 $d=-b$：$f(b+d)=f(0)\ge1>f(b)$，故 $-b\in D(b)$。但 $a+d=a-b<a<0$，$f(a-b)=2^{a-b}<2^a=f(b)=f(a)$，故 $-b\notin D(a)$。
于是 $-b\in D(b)\setminus D(a)$，与 $D(b)\subseteq D(a)$ 矛盾。$\square$

#### 引理 2（POS：$\{f\ge1\}$ 在正半轴是"贴着 0 的初始区间"）
**若 $t>0$ 且 $f(t)\ge1$，则对一切 $s\in(0,t)$ 都有 $f(s)\ge1$。**

*证.* 在 $(\diamond)$ 中取该 $t$、$h=t-s\in(0,t)$、并令 $V\to1^-$（因 $f(t)\ge1>V$ 对所有 $V<1$ 成立）：
$$f(s)=f(t-h)\ge 2^{-h}=2^{-(t-s)}>0.$$
由引理 1，$f(s)>0\Rightarrow f(s)\ge1$。$\square$

#### 引理 3（UP2：$f\le0$ 处严格上升）
**若 $b>0$ 且 $f(b)\le0$，则对一切 $t>b$ 有 $f(t)>f(b)$。**

*证.* 对任意 $a<0$，$f(b)\le0<2^a=f(a)$，即 $f(b)\le f(a)$，由① 得 $D(a)\subseteq D(b)$。
而对 $a<0$ 总有 $(0,-a]\subseteq D(a)$（同 (i) 的论证）。对 $a\to-\infty$ 取并集得 $(0,\infty)\subseteq\bigcup_{a<0}D(a)\subseteq D(b)$。
故对一切 $d>0$ 有 $d\in D(b)$，即 $f(b+d)>f(b)$；令 $t=b+d$ 遍历 $(b,\infty)$ 即得。$\square$

### 主证明：$M=0$，从而 $f$ 在 $(0,\infty)$ 严格递增

由引理 1、2，集合 $\{x>0:f(x)\ge1\}$ 是一个**贴着 0 的初始区间** $(0,M)$（$M\in[0,+\infty]$），其余正半轴 $f\le0$。

**断言：$M=0$，即 $f(x)\le0$ 对一切 $x>0$ 成立。**

反设 $M>0$。取任意 $b\in(0,\min(M,1))\subseteq(0,1)$，则 $f(b)\ge1$（因 $b<M$），同时由条件② $f(b)<f(0)$。
再走一次"尖峰"论证：取 $a<0$，$f(a)=2^a<1\le f(b)$，由① 得 $D(b)\subseteq D(a)$。
取 $d=-b$：$f(b+d)=f(0)>f(b)$（条件②），故 $-b\in D(b)$；而 $a+d=a-b<a<0$，$f(a-b)=2^{a-b}<2^a=f(a)$，故 $-b\notin D(a)$。
得 $-b\in D(b)\setminus D(a)$，矛盾。故 $M=0$，即
$$f(x)\le0\quad\text{对一切 }x>0.$$

于是对任意 $0<u<v$，由引理 3（取 $b=u$，$f(u)\le0$）立得 $f(v)>f(u)$。
**故 $f$ 在 $(0,+\infty)$ 上严格单调递增。** $\blacksquare$

> 备注：约束相容（存在性）。满足全部条件的函数确实存在，例如
> $$f(x)=2^x\ (x<0),\quad f(0)=c\ (\text{任一 }c\ge1),\quad f(x)=-2^{-x}\ (x>0),$$
> 即第 (2) 问那个奇函数（$c=1$ 时）。它在正半轴恒 $\le0$ 且严格增，符合本证明结论。

### 数值实验记录（指导并印证 (ii) 的证明）

| 脚本 | 做的事 | 结果 / 给出的启发 |
|---|---|---|
| `p3ii_2.py`,`_full.py` | 随机/分段线性构造 $f$，在细网格上测条件① | 通过②的上千个 $f$ **几乎全被①否决**，说明①极强 |
| `p3ii_3.py` | 解剖一个"凹坑"反例 $(a,b,d)=(-2,1.5,-1.25)$ | 发现**负点锚 $a$ 的 $D(a)$ 是刚性的**（负 $d$ 进不去），是杠杆所在 |
| `p3ii_diamond_force.py` | 把负点对约束化简 | 推出自相似不等式 $(\diamond)$ |
| `p3ii_recheck.py`,`finalproof.py` | 验证"尖峰" $d=-b$ 落在 $f(0)$ 上的机制 | 锁定 **禁带引理 1**：$(0,1)$ 不可被正半轴取到 |
| `p3ii_diamond_pos.py` | 用 $(\diamond)$ 反推正半轴 | 锁定 **POS 引理 2**：$\{f\ge1\}$ 是初始区间 |
| `p3ii_b2b.py` | 构造"先升到 $\ge1$ 再降到 $\le0$"的 $f$ | 该 $f$ 被 $(\diamond)$ 在负点对 $(-3,-2)$ 处否决 → 印证不能"升后降" |
| `p3ii_final_verify.py`,`robust.py` | 取 $f(x)=-2^{-x}\ (x>0)$ 作为合法例 | $c=1,1.5,2$ 时**通过①②**；$2\times10^6$ 随机点测①**0 反例**；违反禁带/非单调的构造**全部被①否决** |

关键运行输出：
```
CANONICAL f(x)=-2^{-x} on x>0, f(0)=1.0: cond1=(True, None) cond2=True strictly-incr=True
canonical f dense cond① random test fails: 0
viol_band (f∈(0,1) on positives) passes cond①? False   (期望 False ✓)
viol_nonmono (wiggly)            passes cond①? False   (期望 False ✓)
POS-LEMMA 验证: t=1.5 f=1.414>=1, s=0.005 f(s)=-0.498  → 需 >=1 被违反 → 该 f 非法 ✓
```

---

## 结论汇总

| 小问 | 结论 |
|---|---|
| (1) | $D(-1)=\left(0,\dfrac32\right)$（两端开） |
| (2) | $D(x_2)\subseteq D(x_1)$ 成立；按 $x_1,x_2$ 符号分四情形，用 $D(x_0)$ 显式公式逐一验证 |
| (3i) | $f(0)\ge1$（反证 + 在 $(0,-x)\subset(0,1)$ 上撞条件②） |
| (3ii) | $f$ 在 $(0,+\infty)$ 严格递增；核心是先证 **$f(x)\le0\ \forall x>0$**（禁带引理 + POS 初始区间 + 尖峰矛盾迫使 $M=0$），再由 $f\le0$ 处的严格上升引理收尾 |

**harness 工具的价值（针对 (3ii)）**：纯推理很容易卡在"$f(u)\ge f(v)\ge1$ 的硬核情形"上反复打转。数值实验起到了决定性作用——通过构造各种候选 $f$ 并观察**条件①在什么样的 $(a,b,d)$ 上失败**，我直接"看见"了三类失败模式（负点锚刚性、尖峰落在 $f(0)$、$(\diamond)$ 自相似），从而逆推出禁带引理与 POS 引理这两条关键结论，最终把问题归约为干净的"$f(x)\le0\ \forall x>0$"。这是纯 API 无工具模型难以走到的一步。
