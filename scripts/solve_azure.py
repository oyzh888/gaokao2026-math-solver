import sys, requests
from openai import AzureOpenAI
token=open('/sensei-fs-3/users/zouyang/.secrets/pluto-auth-token-steve-train.txt').read().strip()
c=requests.get('https://foundry-aws-pluto.adobe.io/iam/credentials/azure',headers={'x-pluto-token':token},timeout=30).json()
client=AzureOpenAI(azure_ad_token=c["token"],api_version="2025-04-01-preview",azure_endpoint=c["endpoint"])
prompt=open(sys.argv[1]).read(); deploy=sys.argv[2]
kw=dict(model=deploy,messages=[{"role":"user","content":prompt}],max_completion_tokens=40000)
try:
    kw["reasoning_effort"]="medium"
    r=client.chat.completions.create(**kw)
except Exception as e:
    print("retry without reasoning_effort:",e,file=sys.stderr)
    kw.pop("reasoning_effort",None)
    r=client.chat.completions.create(**kw)
print(r.choices[0].message.content or "[EMPTY]")
print(f"\n\n<!-- usage: rt={r.usage.completion_tokens_details.reasoning_tokens} total={r.usage.completion_tokens} -->",file=sys.stderr)
