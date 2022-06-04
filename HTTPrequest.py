import requests

# basic get

r = requests.get('https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol')
print(r.status_code)
print(len(r.content))
print(r.headers['Content-Type'])

# basic post with body

body = {'username': 'Marco', 'password': '11223344'}
r = requests.post('https://httpbin.org/post', data=body)
print(r.text)

# convert request to dict
print(type(r.json()))

# params
par = {'things': 2, 'total': 25}
r = requests.get('https://httpbin.org/get', params=par)
print(r.json())

# headers

headers = {"token": "asdkgbsfdgioanewrf"}
r = requests.get('https://httpbin.org/get', headers=headers)
print(r.json())

