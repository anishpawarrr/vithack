import requests
import json

api_url = "https://v1.genr.ai/api/use-case/generate-lyrics"
params = {"genre": "Rap","artist": "Kanye West"}
response = requests.post(api_url, json=params)
output = json.loads(response.text)
lyrics = output["output"]
print(lyrics)