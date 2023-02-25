import json
import requests
from img import giveimg


api = 'https://v1.genr.ai/api/circuit-element/generate-product-ad'

payload = {
  "product_description": "An api library that simplifies high level generation tasks",
  "temperature": 0.5,
  "platform": "Instagram",
  "target_audience": "Gen Z"
}

headers = {"Content-Type": "application/json"}
response = requests.request("POST", api, json=payload, headers=headers)
url = json.loads(response.text)["output"]
print(url)

