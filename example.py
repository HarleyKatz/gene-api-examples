import json
import os
import requests

BASE_URL = "https://david-gene-api.herokuapp.com/{}"

username = os.environ['USER']
api_key = os.environ['API_KEY']
gene = "CFTR"

# Hit the auth endpoint to get the jwt token

headers = {
    "content-type": "application/json"
}

payload = {
    "username": username,
    "password": api_key
}

r = requests.post(BASE_URL.format("auth"), headers=headers, data=json.dumps(payload)) 

if r.status_code == 200:
    token = r.json()["access_token"]

    headers = {
        "content-type": "application/json",
        "Authorization": f"JWT {token}"
    }

    r = requests.get(BASE_URL.format(f"genes/{gene}"), headers=headers)

    if r.status_code == 200:
        gene_info = r.json()
        print(gene_info)
    else:
        print(f"Error in gene endpoint: {r.content}")
else:
    print(f"Error in auth endpoint: {r.content}")