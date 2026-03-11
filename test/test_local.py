import requests

resp = requests.post("http://localhost:8080", files={'file': open('0.jpg', 'rb')})

print(resp.json())