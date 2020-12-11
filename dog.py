import pip._vendor.requests as requests


API_URL = 'http://shibe.online/api/shibes?count=1'
params = {"count": 10}
response = requests.get(API_URL, params=params)

status_code = response.status_code

print('Status code', status_code)

response_json = response.json()

print(response_json)