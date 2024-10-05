from selenium.webdriver.remote.webdriver import WebDriver
from utils.excel_py.read_excel import create_relative_csv, remove_excel
from utils.scrap_py.naver_trends import getNaverTrends # Type


def create_csvs(brand_list: list, excel_file_path: str, driver: WebDriver):
  for idx, el in enumerate(brand_list):
    if idx % 5 == 0:
      brand_list_5 = []
      if idx+5 > len(brand_list):
        brand_list_5 = brand_list[idx:]
      else:
        brand_list_5 = brand_list[idx:idx+5]
      is_excel_download_success = getNaverTrends(brand_list_5, driver)
      if (is_excel_download_success):
          print('Excel download success')
          keywords_list = create_relative_csv(excel_file_path)
          print(f"{keywords_list} csv file created")
          remove_excel(excel_file_path)