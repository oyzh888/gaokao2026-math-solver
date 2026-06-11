#!/usr/bin/env python3
"""读取各模型解答 md，转 HTML，注入评分数据到 compare.html。"""
import json, re, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNS = ROOT / "solutions/problem_19/model_runs"
OUT  = ROOT / "solutions/problem_19/compare.html"

# 模型清单 + 人工评分（依据逐题对照标答；(3ii)从宽）
# sym: ✅ 完整严格 / 🟡 结论对但跳步 / ❌ 错或缺 / — 未产出
# group: "harness" = Claude Code agentic harness（有工具，能写代码自验证）
#        "api"     = 纯 API 单次调用（无工具）
MODELS = [
  # ===== Claude Code harness 组（带工具）=====
  dict(group="harness", key="harness_opus", model="Claude Opus 4.8", vendor="Claude Code (harness)", vcls="anthropic",
       q1="✅", q2="✅", q3i="✅", q3ii="✅", overall="✅ 满分级", medal="🥇",
       meta="51 次工具调用 · 200万随机点验证 · 归纳失败模式逆推出『禁带引理』，在 (3ii) 上比纯推理走得更远"),
  dict(group="harness", key="harness_sonnet", model="Claude Sonnet 4.6", vendor="Claude Code (harness)", vcls="anthropic",
       q1="✅", q2="✅", q3i="✅", q3ii="✅", overall="✅ 满分级", medal="🥇",
       meta="15 次工具调用 · 写脚本数值验证 (1)(2)(3i)(3ii) · 9步矛盾链全部代码核对"),

  # ===== 纯 API 组（无工具，单次调用）=====
  dict(group="api", key="azure_gpt-5.5", model="GPT-5.5", vendor="OpenAI (Azure)", vcls="openai",
       q1="✅", q2="✅", q3i="✅", q3ii="✅", overall="✅ 满分级", medal="🥇",
       meta="reasoning≈15k tok · 引理法完整证 (3ii)"),
  dict(group="api", key="gemini_gemini-2.5-pro", model="Gemini 2.5 Pro", vendor="Google", vcls="google",
       q1="✅", q2="✅", q3i="✅", q3ii="✅", overall="✅ 满分级", medal="🥇",
       meta="显式构造迭代序列 x₁-ky 制造矛盾，最严谨"),
  dict(group="api", key="gemini_gemini-3.5-flash", model="Gemini 3.5 Flash", vendor="Google", vcls="google",
       q1="✅", q2="✅", q3i="✅", q3ii="✅", overall="✅ 满分级", medal="🥇",
       meta="最新 flash 模型；引理『f(x)≥1 on (0,∞)』+ 负半轴矛盾，完整严格"),
  dict(group="api", key="gemini_gemini-3.1-pro-preview", model="Gemini 3.1 Pro", vendor="Google", vcls="google",
       q1="✅", q2="✅", q3i="✅", q3ii="🟡", overall="🟡 接近", medal="🥈",
       meta="证出 f∉(0,1) 关键结论；末步『无限细分』表述含糊"),
  dict(group="api", key="claude_haiku", model="Claude Haiku 4.5", vendor="Anthropic", vcls="anthropic",
       q1="✅", q2="✅", q3i="✅", q3ii="🟡", overall="🟡 接近", medal="🥈",
       meta="纯 API；(3i) 递推证法漂亮；(3ii) 末步概述不严"),
  dict(group="api", key="gemini_gemini-3.1-flash-lite", model="Gemini 3.1 Flash-Lite", vendor="Google", vcls="google",
       q1="✅", q2="🟡", q3i="🟡", q3ii="🟡", overall="🟡 思路对", medal="",
       meta="最小模型；(1) 正确，(2)(3) 框架对但推导略简"),
  dict(group="api", key="bedrock_opus", model="Claude Opus 4.8", vendor="Anthropic", vcls="anthropic",
       q1="✅", q2="🟡", q3i="🟡", q3ii="🟡", overall="🟡 思路对", medal="",
       meta="纯 API（无工具）；探索式草稿，导出强结论但未收尾——对比 harness 版差距明显"),
  dict(group="api", key="bedrock_sonnet", model="Claude Sonnet 4.6", vendor="Anthropic", vcls="anthropic",
       q1="✅", q2="🟡", q3i="🟡", q3ii="❌", overall="🟡 部分", medal="",
       meta="纯 API（无工具）；(3ii) 自陈『没找到矛盾』未完成——对比 harness 版差距明显"),
  dict(group="api", key="azure_gpt-5", model="GPT-5", vendor="OpenAI (Azure)", vcls="openai",
       q1="—", q2="—", q3i="—", q3ii="—", overall="— 超时", medal="",
       meta="reasoning effort 过重，多次超时未产出"),

  # ===== 老模型组（看代际进步；纯 API，单次调用）=====
  dict(group="legacy", key="azure_gpt-5-mini", model="GPT-5 mini", vendor="OpenAI (Azure)", vcls="openai",
       q1="✅", q2="🟡", q3i="✅", q3ii="🟡", overall="🟡 接近", medal="",
       meta="小模型却很扎实：(1) 正确算出 (0,3/2)，(3i) 严格，(3ii) 给出正确的『取 2^y→1 制造矛盾』构造思路但收尾略简"),
  dict(group="legacy", key="gemini_gemini-2.5-flash-lite", model="Gemini 2.5 Flash-Lite", vendor="Google", vcls="google",
       q1="✅", q2="🟡", q3i="🟡", q3ii="🟡", overall="🟡 思路对", medal="",
       meta="老一档 flash-lite；(1) 正确，(2)(3) 中英混杂、反复试探，(3ii) 末步『this implies f is increasing』含糊"),
  dict(group="legacy", key="bedrock_claude35_haiku", model="Claude 3.5 Haiku", vendor="Anthropic", vcls="anthropic",
       q1="❌", q2="🟡", q3i="🟡", q3ii="🟡", overall="❌ 偏弱", medal="",
       meta="2024-10；(1) 答错 (-1,2)，(2)(3) 仅条列要点、循环论证，未真正展开"),
  dict(group="legacy", key="bedrock_claude3_sonnet", model="Claude 3 Sonnet", vendor="Anthropic", vcls="anthropic",
       q1="❌", q2="🟡", q3i="❌", q3ii="❌", overall="❌ 偏弱", medal="",
       meta="2024-02；(1) 答错 (-∞,-1)，(3i) 用『f(x)≠0 恒成立』错误推理，(3ii) 把要证的当条件——循环论证"),
  dict(group="legacy", key="bedrock_claude3_haiku", model="Claude 3 Haiku", vendor="Anthropic", vcls="anthropic",
       q1="❌", q2="❌", q3i="❌", q3ii="❌", overall="❌ 做不动", medal="",
       meta="2024-03；最老一档；(1) 答错 {d<0}，各问基本复述题面/循环论证，体现两年来的代际差距"),
]

md = markdown.Markdown(extensions=["fenced_code","tables"])

def to_html(key):
    f = RUNS / f"{key}.md"
    if not f.exists() or f.stat().st_size == 0:
        return None
    txt = f.read_text(encoding="utf-8", errors="ignore")
    # strip usage comment
    txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)
    # protect math from markdown mangling: $$..$$, \[..\], \(..\), $..$
    holds=[]
    def stash(m):
        holds.append(m.group(0)); return f"@@MJ{len(holds)-1}@@"
    txt = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|\$[^\$\n]+?\$", stash, txt, flags=re.S)
    html = md.convert(txt); md.reset()
    for i,h in enumerate(holds):
        html = html.replace(f"@@MJ{i}@@", h)
    return html

rows=[]; answers=[]
for m in MODELS:
    html = to_html(m["key"])
    rows.append({k:m[k] for k in ("group","model","vendor","vcls","q1","q2","q3i","q3ii","overall","medal")})
    answers.append(dict(group=m["group"], model=m["model"], vendor=m["vendor"], vcls=m["vcls"], meta=m["meta"],
                        html=html or "<p style='color:#93a1b5'>（该模型解答尚未产出 / 凭证待补）</p>"))

page = OUT.read_text(encoding="utf-8")
payload = json.dumps({"rows": rows, "answers": answers}, ensure_ascii=False)
payload = (payload.replace(chr(0x2028), "\\u2028").replace(chr(0x2029), "\\u2029")
                  .replace("</", "<\\/"))
data_js = ("\n/*DATA*/\n"
           "const _P=JSON.parse(document.getElementById('payload').textContent);\n"
           "const SCORE={rows:_P.rows};\n"
           "const ANSWERS=_P.answers;\n"
           "/*ENDDATA*/\n")
page = re.sub(r"\n/\*DATA\*/[\s\S]*?/\*ENDDATA\*/\n", data_js, page, count=1)
# inject/replace the JSON payload script before <script id="data">
block = '<script id="payload" type="application/json">' + payload + '</script>\n'
page = re.sub(r'<script id="payload"[\s\S]*?</script>\n', "", page, count=1)
page = page.replace('<script id="data">', block + '<script id="data">', 1)
OUT.write_text(page, encoding="utf-8")
print("injected", len(rows), "models;", sum(1 for a in answers if "尚未" not in a["html"]), "have answers")
