import requests
from bs4 import BeautifulSoup

# pip install requests
# pip install beautifulsoup4 cmd에 입력하기

url = "https://quotes.toscrape.com/"
response = requests.get(url)
print(response)

# 요청이 성공했는지 확인
if response.status_code == 200 : 
    #HTML 문서를 파싱
    soup = BeautifulSoup(response.text,
    "html.parser")
 
    quotes = soup.find_all("div", class_ ="quote")
    
    result = {}
    for quote in quotes :
        text = quote.find("span", class_="text").get_text()
        r_text = text[1:-2]
        #r_text = text.replace('"'," ")
        author = quote.find("small", class_="author").get_text()
        
        result[author] = r_text

        print(result)