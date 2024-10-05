from selenium.webdriver.remote.webdriver import WebDriver # Type
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

# 네이버 광고 플랫폼 접속
brand_list = ['라코스테', '빈폴', '타미힐피거', '폴로 랄프 로렌', '헤지스', '브룩스브라더스', '시리즈', '안데르센안데르센', '질스튜어트', '헨리코튼', '에디션', '지이크', '스톤 아일랜드', '폴 스미스', '아크네 스튜디오', 'APC', '메종 키츠네', '칼하트', '스튜디오 톰보이', '커스텀멜로우', 'Coor', '앤더슨벨', '아더에러', '드로우핏', '인사일러스', '브라운야드', '마르디 메크르디', '마뗑킴', '포터리']

def get_monthly_search_volume(keyword: str, driver: WebDriver) -> int:
  url = 'https://manage.searchad.naver.com/customers/1261829/tool/keyword-planner'
  driver.get(url)

  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#keyword-hint'))
  )
  search_text_area = driver.find_element(By.CSS_SELECTOR, 'textarea#keyword-hint')
  search_text_area.send_keys(keyword)
  time.sleep(2)

  # 조회하기 버튼 클릭
  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.col-keyword-query button.btn'))
  )
  search_button = driver.find_element(By.CSS_SELECTOR, '.col-keyword-query button.btn.btn-primary')
  search_button.click()

  time.sleep(3)

  # 월간 검색량 구하기
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody.data-table-tbody tr td[style="text-align: center;"]'))
  )
  first_tr = driver.find_element(By.CSS_SELECTOR, 'tbody.data-table-tbody tr')
  # 월별 검색량을 계산할 때, 쉼표 제거 후 정수로 변환
  monthly_search_volume = (
      int(first_tr.find_elements(By.CSS_SELECTOR, 'td')[2].text.replace(',', '')) +
      int(first_tr.find_elements(By.CSS_SELECTOR, 'td')[3].text.replace(',', ''))
  )
  return monthly_search_volume
