import re

import requests
from selenium import webdriver
from time import sleep

i = 16
# url = str('https://ting55.com/book/13679-%d' % (i))


while i < 752:
    driver = webdriver.Chrome()
    driver.get('https://m.ting55.com/book/13679-%d' % (i))
    src = driver.find_element_by_xpath('//*[@id="player"]').get_attribute('src')
    print(src)

    r = requests.get('https://m.ting55.com/book/13679-%d' % (i))

    path = "%s.mp3" % (i)
    print(path)

    with open(path, "wb") as f:
        f.write(r.content)
    f.close()
    i += 1
    sleep(1)
    driver.quit()
