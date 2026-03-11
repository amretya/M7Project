import requests
import json

url = "http://localhost:8080/predict"

payload = {
    "text": "I worked very hard on this project and now I feel proud but exhausted."
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))