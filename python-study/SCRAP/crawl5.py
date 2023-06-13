from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time
import os
import pyperclip

url = "https://naver.com"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#네이버 로그인 버튼 클릭
#<a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https://www.naver.com/" class="MyView-module__link_login___HpHMW"><i class="MyView-module__naver_logo____Y442"><span class="blind">NAVER</span></i>로그인</a>
driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW").click()
time.sleep(3)

#네이버 아이디, 패스워드
naver_id = "minseonnn"
naver_pw = "#Alstjs21"

# 네이버 아이디 입력창
# driver.find_element(By.ID, 'id').send_keys(naver_id)
id_input = driver.find_element(By.ID, 'id')
pyperclip.copy(naver_id) # control + c
id_input.click()
id_input.send_keys(Keys.CONTROL, 'v') # control + v
time.sleep(2)

#네이버 패스워드 입력
# send_key 는  컴퓨터에 입력되어 지는 값 , time.sleep은 로딩 시간 
# driver.find_element(By.ID, 'pw').send_keys(naver_pw)
pw_input = driver.find_element(By.ID, 'pw')
pw_input.click()
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

#로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(10)


# 지금은 오류 뜨는데 집에서 한번 해보기