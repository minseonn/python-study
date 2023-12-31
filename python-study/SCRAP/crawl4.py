# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time

url = "https://naver.com"

driver = webdriver.Chrome()
#페이지에 접근
driver.get(url)
#멈추기
time.sleep(1)

# 네이버 검색창에 "인공지능" 텍스트 입력
# <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
#아이디로 찾기:  
driver.find_element(By.ID, "query").send_keys("인공지능")
# 클래스 이용하기 : driver.find_element(By.CLASS_NAME, "search_input").send_keys("한국")
# css 이용하기 : driver.find_element(By.CSS_SELECTOR, '[placeholder="검색어를 입력해 주세요."]').send_keys("미국")
# xpath 이용하기 driver.find_element(By.XPATH, '//*[@id="query"]').send_keys("파이썬")
time.sleep(2)

# 1. 검색창에 enter키 누르기
driver.find_element(By.ID, "query").send_keys(Keys.ENTER)

# 2. 검색 버튼 클릭하기
# <button type="submit" class="btn_search" onclick="window.nclk_v2(this,&quot;sch.action&quot;)"> <span id="search-btn" class="ico_btn_search"></span> <span class="blind">검색</span> </button>
#driver.find_element(By.CLASS_NAME, "btn_search").click()

time.sleep(2)


# 뉴스탭 클릭하기
# <a role="tab" href="?where=news&amp;sm=tab_jum&amp;query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5" onclick="return goOtherCR(this,'a=tab*n.jmp&amp;r=4&amp;i=&amp;u='+urlencode(this.href));" class="tab" aria-selected="false">뉴스</a>
driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[4]/a').click()
time.sleep(2)

#현재 페이지의 뉴스 제목 가져오는 함수
def get_page_news_title() :
    #html 코드 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    # 뉴스 
    news = soup.find_all('li', class_= 'bx')

    for n in news :
        title = n.find("a", class_ = "news_tit")
        if title is not None :
            result = title.get_text()
            print(result)


# 다음 페이지로 이동하는 함수
# <a href="?where=news&amp;sm=tab_pge&amp;query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&amp;sort=0&amp;photo=0&amp;field=0&amp;pd=0&amp;ds=&amp;de=&amp;cluster_rank=65&amp;mynews=0&amp;office_type=0&amp;office_section_code=0&amp;news_office_checked=&amp;nso=so:r,p:all,a:all&amp;start=11" role="button" class="btn_next" aria-disabled="false" onclick="return goOtherCR(this, 'a=nws.paging&amp;r=2&amp;u='+urlencode(urlexpand(this.href)));"><i class="spnew ico_page_arr">다음</i></a>

def click_next_btn() :
    driver.find_element(By.CLASS_NAME, "btn_next").click()
    time.sleep(2)
# 반복문으로 10 번 반복해서 news 타이틀 뽑아오고 next_btn 누르기
for i in range(10) :
    get_page_news_title()
    click_next_btn()


