import json
import requests
from img import giveimg

def givecap(url):
  api = 'https://v1.genr.ai/api/circuit-element/generate-captions'

  payload = {
    "img_url": url,
    "n_words": 15
  }

  headers = {"Content-Type": "application/json"}
  response = requests.request("POST", api, json=payload, headers=headers)
  cap = json.loads(response.text)["output"]
  return cap

