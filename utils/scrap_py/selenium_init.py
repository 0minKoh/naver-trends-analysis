from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Set Chrome options
## /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"

def initSelenium():
  # 원격 디버깅 포트 설정
  remote_debugging_port = 9222
  # 원격 디버깅 포트로 웹 드라이버 초기화
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option(
      "debuggerAddress", f"127.0.0.1:{remote_debugging_port}"
  )
  driver = webdriver.Chrome(options=chrome_options)
  return driver