import re

import requests
from selenium import webdriver
from time import sleep

i = 128
# url = str('https://ting55.com/book/13679-%d' % (i))


while i < 752:
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://ting55.com/glink",  # 必须带这个参数，不然会报错
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    }

    urls = 'https://m.ting55.com/book/13679-%d' % i
    print('链接：' + urls)
    response = requests.get(urls, headers=header)
    print('返回结果：' + response.text)
    content = re.findall(r'"([a-zA-Z0-9]+)"', str(response.text))
    xt = (content[2])
    print('正则结果：' + xt)
    headers = {
        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        # # 'Accept-Encoding': ' gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '27',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': 'JSESSIONID=D53AB7AA0FA4AED301275B735387A161; Hm_lvt_ac3da4632dc24e9d361235e3b2d3a131=1577072216; Hm_lpvt_ac3da4632dc24e9d361235e3b2d3a131=1577087799; ting55_history=https%3A%2F%2Fting55.com%2Fbook%2F13679-2%2560%25E5%25BA%2586%25E4%25BD%2599%25E5%25B9%25B4%25EF%25BC%2588%25E9%2597%25AB%25E9%2581%2593%25E4%25B9%258B%25EF%25BC%2589%25E6%259C%2589%25E5%25A3%25B0%25E5%25B0%258F%25E8%25AF%25B4%25E7%25AC%25AC2%25E7%25AB%25A0',
        'Cookie':'JSESSIONID=D53AB7AA0FA4AED301275B735387A161; Hm_lvt_ac3da4632dc24e9d361235e3b2d3a131=1577072216; Hm_lpvt_ac3da4632dc24e9d361235e3b2d3a131=1577094442; ting55_history=https%3A%2F%2Fting55.com%2Fbook%2F13679-1%2560%25E5%25BA%2586%25E4%25BD%2599%25E5%25B9%25B4%25EF%25BC%2588%25E9%2597%25AB%25E9%2581%2593%25E4%25B9%258B%25EF%25BC%2589%25E6%259C%2589%25E5%25A3%25B0%25E5%25B0%258F%25E8%25AF%25B4%25E7%25AC%25AC1%25E7%25AB%25A0',
        # 'Host': ' ting55.com',
        #'Origin': 'https://ting55.com',
        'Referer': 'https://ting55.com/book/13679-2',
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        'X-Requested-With': 'XMLHttpRequest',
        'xt': 'f2f08f6293157d75717e91d96b947ac'
    }
    headers['xt'] = xt
    headers['Referer'] = urls
    print(headers)
    url = 'https://m.ting55.com/glink'
    data = {'bookId': '13679', 'isPay': '0', 'page': '%d' % i}
    #print(data)
    r = requests.post(url, data, headers=headers)

    print(r.text)
    durl = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(r.text))
    print(durl[0])
    #     # driver = webdriver.Chrome()
    #     # driver.get('https://ting55.com/book/13679-%d' % (i))
    #     # src = driver.find_element_by_xpath('//*[@id="jp_audio_0"]').get_attribute('src')
    #     # print(src)
    #
    books = requests.get(durl[0])

    path = "%s.mp3" % (i)
    print(path)

    with open(path, "wb") as f:
        f.write(books.content)
    f.close()
    i += 1
#     sleep(3)
#     #driver.quit()
