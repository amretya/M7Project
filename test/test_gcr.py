import requests
import json

url = "https://m7projectemotion-383117336731.asia-southeast1.run.app/predict"

payload = {
    "text": "I worked very hard on this project and now I feel proud but exhausted."
}

response = requests.post(url, json=payload, timeout=120)

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))