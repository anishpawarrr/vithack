import json
import requests
from img import giveimg

api = 'https://v1.genr.ai/api/circuit-element/generate-captions'

payload = {
  "img_url": giveimg('blue bottle'),
  "n_words": 15
}

headers = {"Content-Type": "application/json"}
response = requests.request("POST", api, json=payload, headers=headers)
url = json.loads(response.text)["output"]
print(url)

