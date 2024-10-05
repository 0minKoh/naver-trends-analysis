from utils.scrap_py.selenium_init import initSelenium
from utils.scrap_py.naver_trends import getNaverTrends

brand_list = ['라코스테', '빈폴', '타미힐피거', '폴로 랄프 로렌', '헤지스', '브룩스브라더스', '시리즈', '안데르센안데르센', '질스튜어트', '헨리코튼', '에디션', '지이크', '스톤 아일랜드', '폴 스미스', '아크네 스튜디오', 'APC', '메종 키츠네', '칼하트', '스튜디오 톰보이', '커스텀멜로우', 'Coor', '앤더슨벨', '아더에러', '드로우핏', '인사일러스', '브라운야드', '마르디 메크르디', '마뗑킴', '포터리']

# Set Chrome options
## /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"

# Crawler Initialization
try:
  driver = initSelenium()
  brand_list_5 = brand_list[:5]
  is_excel_download_success = getNaverTrends(brand_list_5, driver)
  if (is_excel_download_success):
      print('Excel download success')
except KeyboardInterrupt as e:
  print(f'프로그램 종료! ')



