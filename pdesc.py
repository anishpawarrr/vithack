import json
import requests
from img import giveimg

def givead(desc, pltfrm, audi):
  api = 'https://v1.genr.ai/api/circuit-element/generate-product-ad'

  payload = {
    "product_description": desc,
    "temperature": 0.5,
    "platform": pltfrm,
    "target_audience": audi
  }

  headers = {"Content-Type": "application/json"}
  response = requests.request("POST", api, json=payload, headers=headers)
  ad = json.loads(response.text)["output"]
  return ad


