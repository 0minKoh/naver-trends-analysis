from utils.excel_py.create_csvs import create_csvs
from utils.scrap_py.selenium_init import initSelenium
from utils.scrap_py.naver_trends import getNaverTrends
from utils.excel_py.read_excel import create_relative_csv, remove_excel
from utils.scrap_py.naver_ads_keywords import get_monthly_search_volume
from utils.excel_py.update_csvs import get_202409_relative_volumn, update_relative_to_absolute_value, update_csvs

# Set Chrome options
## /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
excel_file_path = 'assets/excel_naver_trends'

# Crawler Initialization
try:
  driver = initSelenium()
  # Create CSVs (Scrap Naver Trends)
  ## create_csvs(brand_list, excel_file_path, driver)

  groups = [
    ['라코스테', '빈폴', '타미힐피거', '폴로 랄프 로렌', '헤지스'],
    ['브룩스브라더스', '시리즈', '안데르센안데르센', '질스튜어트', '헨리코튼'],
    ['에디션', '지이크', '스톤 아일랜드', '폴 스미스', '아크네 스튜디오'],
    ['APC', '메종 키츠네', '칼하트', '스튜디오 톰보이', '커스텀멜로우'],
    ['Coor', '앤더슨벨', '아더에러', '드로우핏', '인사일러스'],
    ['브라운야드', '마르디 메크르디', '마뗑킴', '포터리']
  ]

  for idx, group in enumerate(groups):
    monthly_volume = get_monthly_search_volume(group[0], driver)
    total_relative_volumn = get_202409_relative_volumn(f'res/{group[0]}.csv', group[0])
    search_volume_per_relative = update_relative_to_absolute_value(total_relative_volumn, monthly_volume)

    # update CSVs
    for brand in group:
      updated_df = update_csvs(f'res/{brand}.csv', search_volume_per_relative)
      print("Updated: ", brand)


except KeyboardInterrupt as e:
  print(f'프로그램 종료! ')



