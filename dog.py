import pip._vendor.requests as requests


API_URL = 'http://shibe.online/api/shibes?count=1'

response = requests.get(API_URL)

status_code = response.status_code

print('Status code', status_code)