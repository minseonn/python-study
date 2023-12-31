#오늘 서울,11의 날씨 예보

import requests
from bs4 import BeautifulSoup

#웹 페이지에 get 요청을 보냅니다.
url = "https://weather.com/ko-KR/weather/today/l/KSXX0037:1:KS?Goto=Redirected"
response = requests.get(url)


# 요청이 성공했는지 확인합니다.
if response.status_code == 200 :
    #html 문서를 beautifulSoup로 파싱합니다.
    soup = BeautifulSoup(response.text, "html.parser")

    #오늘 날씨 정보를 포함하는 요소를 찾습니다.
    weathers = soup.find_all("div", class_ = "ListItem--listItem--25ojW")

    # 각 정보 데이터를 출력합니다.
    result= {}
    for weather in weathers:
        key_name =  weather.find("div", class_="WeatherDetailsListItem--label--2ZacS").get_text()
        value = weather.find("div", class_ = "WeatherDetailsListItem--wxData--kK35q").get_text()
        result[key_name] = value
        
    print(result)

