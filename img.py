import requests
import  json
api = "https://v1.genr.ai/api/circuit-element/generate-image"

def giveimg(des):
    payload = {
        "prompt": des,
        "height": 512,
        "width": 512,
        "model": "dall-e",
        "n_images": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", api, json=payload, headers=headers)
    url = json.loads(response.text)["output"]
    print(url)
    return url



#
# prom = input("Enter prompt->")
# payload = {
#     "prompt": prom,
#     "height": 512,
#     "width": 512,
#     "model": "stable-diffusion",
#     "n_images": 1
# }
# headers = {"Content-Type": "application/json"}
# response = requests.request("POST", api, json=payload, headers=headers)
# url = json.loads(response.text)["output"]
# print(url)
