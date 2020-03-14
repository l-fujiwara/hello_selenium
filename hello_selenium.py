import time
from selenium import webdriver

# ダウンロードしたドライバの場所を指定します
driver = webdriver.Chrome('driver/chromedriver.exe')

# URLを開く
driver.get('https://www.yahoo.co.jp/')

# 検索ボックスに文字を入力する
driver.find_element_by_xpath('//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/input').send_keys('selenium')

# 検索ボタンをクリックする
driver.find_element_by_xpath('//*[@id="ContentWrapper"]/header/section[1]/div/form/fieldset/span/button/span/span').click()

print('10秒待ってからブラウザを終了します')
time.sleep(10)
driver.quit()
