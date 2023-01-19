import requests

# es1
print(requests.get("http://localhost:3333/es1").text)

# es2
print(requests.get("http://localhost:3333/es2", params={"x": 2, "y": 57}).text)

# es4
print(requests.post("http://localhost:3333/es3", params={"filter": "ipp"}, json={"pippo": 2, "pluto": 57}).json())
