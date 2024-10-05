from selenium.webdriver.remote.webdriver import WebDriver # Type
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

# Naver Trends Excel 다운로드
def getNaverTrends(keywords_list: list, driver: WebDriver) -> bool:
    # Naver Trends URL
    url = 'https://datalab.naver.com/keyword/trendSearch.naver'
    driver.get(url)

    # 키워드 검색
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input#item_keyword1'))
    )
    time.sleep(3)

    item_keyword_input1 = driver.find_element(By.CSS_SELECTOR, 'input#item_keyword1')
    item_keyword_input2 = driver.find_element(By.CSS_SELECTOR, 'input#item_keyword2')
    item_keyword_input3 = driver.find_element(By.CSS_SELECTOR, 'input#item_keyword3')
    item_keyword_input4 = driver.find_element(By.CSS_SELECTOR, 'input#item_keyword4')
    item_keyword_input5 = driver.find_element(By.CSS_SELECTOR, 'input#item_keyword5')

    # keywords_list의 길이가 5보다 크면 에러 발생
    if len(keywords_list) > 5:
        raise ValueError('키워드는 5개 이하로 입력해주세요.')

    for idx, keyword in enumerate(keywords_list):
        if idx == 0:
            item_keyword_input1.send_keys(keyword)
        elif idx == 1:
            item_keyword_input2.send_keys(keyword)
        elif idx == 2:
            item_keyword_input3.send_keys(keyword)
        elif idx == 3:
            item_keyword_input4.send_keys(keyword)
        elif idx == 4:
            item_keyword_input5.send_keys(keyword)

    # 기간 설정
    ## 2016년 1월 1일 ~ 2024년 9월 30일
    start_year_input = driver.find_element(By.CSS_SELECTOR, 'input#startYearInput')
    driver.execute_script(f"arguments[0].value = '2019'", start_year_input)
    start_month_input = driver.find_element(By.CSS_SELECTOR, 'input#startMonthInput')
    driver.execute_script(f"arguments[0].value = '01'", start_month_input)
    start_day_input = driver.find_element(By.CSS_SELECTOR, 'input#startDayInput')
    driver.execute_script(f"arguments[0].value = '01'", start_day_input)

    end_year_input = driver.find_element(By.CSS_SELECTOR, 'input#endYearInput')
    driver.execute_script(f"arguments[0].value = '2024'", end_year_input)

    end_month_input = driver.find_element(By.CSS_SELECTOR, 'input#endMonthInput')
    driver.execute_script(f"arguments[0].value = '09'", end_month_input)

    end_day_input = driver.find_element(By.CSS_SELECTOR, 'input#endDayInput')
    driver.execute_script(f"arguments[0].value = '30'", end_day_input)
    
    # 네이버 검색 데이터 조회 버튼 클릭
    search_button = driver.find_element(By.CSS_SELECTOR, 'a.ca_btn_go._trend_search_detail_query') 
    search_button.click()

    # 엑셀 다운로드 버튼 클릭
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.sp_btn_file_down'))
    )
    time.sleep(3)
    excel_download_button = driver.find_element(By.CSS_SELECTOR, 'a.sp_btn_file_down')
    excel_download_button.click()

    # 다운로드 완료까지 대기
    excel_download_path = '/Users/sohyunwoo/Desktop/developer/python_personal/naver-trends/assets/excel_naver_trends'
    while True:
        time.sleep(2)
        files: list = os.listdir(excel_download_path)
        first_file: str = files[0]
        if first_file:
            # 첫 번째 파일이 excel 파일인지 확인
            if first_file.endswith('.xlsx'):
                break
            else:
                continue
        else:
            continue
    return True



