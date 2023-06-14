# o66VTItZIwqrzjLKTbZmUKkTWd5oXLSympNWWQAMkqVThcNQ68sAKIUdG-Rvgkph6Yk_bgo9dRoAAAGIt8ttUA
import urllib.request
import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "952c98aeea3ffd1ad58996cb781806f9",
    "redirect_uri" : "http://localhost",
    "code" : "HVQGjp_m4dlErogvyWL5J-SwAJPpeEjRwuCN4-ayCIAaXC4wQJ7otiKlVt_Hbqdv1B-zjgorDNMAAAGIt_N7ag" #발급받은 코드
}

response = requests.post(url, data=data)
tokens = response.json()

# 토큰을 파일로 저장하기
if "access_token" in tokens:
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)
        print("Tokens saved successfully")
else:
    print(tokens)