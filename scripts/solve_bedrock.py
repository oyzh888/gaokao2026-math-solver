import sys, os, json, urllib.request
region=os.environ["AWS_REGION"]; tok=os.environ["AWS_BEARER_TOKEN_BEDROCK"]
model=sys.argv[2]; prompt=open(sys.argv[1]).read()
url=f"https://bedrock-runtime.{region}.amazonaws.com/model/{model}/invoke"
body=json.dumps({"anthropic_version":"bedrock-2023-05-31","max_tokens":20000,
    "messages":[{"role":"user","content":prompt}]}).encode()
req=urllib.request.Request(url,data=body,method="POST",
    headers={"Authorization":f"Bearer {tok}","Content-Type":"application/json","Accept":"application/json"})
r=urllib.request.urlopen(req,timeout=600)
d=json.load(r)
print("".join(b.get("text","") for b in d.get("content",[])))
