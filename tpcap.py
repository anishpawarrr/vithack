import requests

url = "https://v1.genr.ai/api/circuit-element/generate-captions"

payload = {
    "img_url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-S5slvMoYAyvlprF4lKs5jt16/user-MAvKx76Taxh2gIdCWn8xnqpY/img-ZLgkKV4rXPaPEIv7szcYbQKj.png?st=2023-02-25T06%3A43%3A43Z&se=2023-02-25T08%3A43%3A43Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-24T15%3A23%3A07Z&ske=2023-02-25T15%3A23%3A07Z&sks=b&skv=2021-08-06&sig=lyMc1Wv83LgRT7IIgsM5Yz%2BLNNUEUR70daY8qN6FfJ4%3D",
    "n_words": 15
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)