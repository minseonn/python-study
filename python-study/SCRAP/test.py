import requests

url = "http://apis.data.go.kr/5530000/hs-coronavirus-coronic/getHsCoronavirusCoronic?serviceKey=phjcxX9fpBpaVqae%2FNeAbsqHmCRoSagQ9Ur8NCHwAmoEA1hOXrdmFNkRjxgKyhem5Bm0Fy3ewn%2BLj905PnAN0A%3D%3D&pageNo=1&numOfRows=10"

payload = {}
headers = {}

response = requests.get(url, verify=False)

print(response.text)
