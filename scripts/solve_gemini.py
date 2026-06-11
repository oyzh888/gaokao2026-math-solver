import sys, requests
from google.oauth2.credentials import Credentials
from google import genai
token = open("/sensei-fs-3/users/zouyang/.secrets/pluto-auth-token-steve-train.txt").read().strip()
data = requests.get("https://foundry-aws-pluto.adobe.io/iam/credentials/gcp",
                    headers={"x-pluto-token": token}, timeout=30).json()
creds = Credentials(token=data["token"])
client = genai.Client(vertexai=True, project=data["project_id"], location="global", credentials=creds)
prompt = open(sys.argv[1]).read()
model = sys.argv[2]
r = client.models.generate_content(model=model, contents=prompt)
print(r.text)
