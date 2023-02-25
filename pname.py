import json

import requests
def givename(prom):
    url = "https://v1.genr.ai/api/circuit-element/generate-product-name"

    payload = {
        "product_description": prom,
        "temperature": 0.8,
        "keywords": ""
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    l = response.text.split('Product names:')
    print(l)
    s = l[1][:-3]
    rlist = s.split(',')
    print(rlist)
    return rlist
givename('donald trump riding horse')
