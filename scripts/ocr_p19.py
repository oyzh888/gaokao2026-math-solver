import requests
from google.oauth2.credentials import Credentials
from google import genai
from google.genai import types

token = open("/sensei-fs-3/users/zouyang/.secrets/pluto-auth-token-steve-train.txt").read().strip()
data = requests.get("https://foundry-aws-pluto.adobe.io/iam/credentials/gcp",
                    headers={"x-pluto-token": token}, timeout=30).json()
creds = Credentials(token=data["token"])
client = genai.Client(vertexai=True, project=data["project_id"], location="global", credentials=creds)

imgs=[]
for p in ["paper/gk100_pages/page_11.png","paper/gk100_pages/page_12.png"]:
    imgs.append(types.Part.from_bytes(data=open(p,'rb').read(), mime_type="image/png"))

prompt = """这两张图是2026新高考I卷数学试卷扫描页(含答案解析)。请精确转录第19题。
要求:
1. 只转录【第19题】的题干(原始题目),不要转录解析部分。用 LaTeX 数学记号。
2. 单独把图中【解析/答案】部分的第19题完整解答也转录出来(用 LaTeX)。
3. 输出严格分两块: 
=== 题干 ===
...
=== 标准答案/解析 ===
...
忠实转录,不要自己改写或解题。看不清的地方标 [?]。"""

r = client.models.generate_content(model="gemini-3.1-pro-preview", contents=[prompt, *imgs])
print(r.text)
