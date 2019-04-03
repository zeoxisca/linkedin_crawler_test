#-*-  coding:utf-8 -*-

import random
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random


chromeOptions = webdriver.ChromeOptions()
link = []
aims = []
# countries = ['ae', 'af', 'ag', 'al', 'am', 'as', 'at', 'az', 'ba', 'be', 'bf', 'bg', 'bi', 'bj', 'bo', 'bs', 'bt', 'by', 'ca', 'cc', 'cf', 'cg', 'ch', 'ci', 'cl', 'cm', 'co', 'cv', 'cz', 'de', 'dj', 'dk', 'dm', 'dz', 'ec', 'ee', 'es', 'fi', 'fm', 'fr', 'ga', 'ge', 'gf', 'gl', 'gm', 'gp', 'gr', 'gy', 'hk', 'hn', 'hr', 'ht', 'hu', 'ie', 'in', 'iq', 'is', 'it', 'jo', 'jp', 'kg', 'ki', 'kz', 'la', 'li', 'lk', 'lt', 'lu', 'lv', 'ma', 'md', 'mg', 'ml', 'mn', 'ms', 'mv', 'mw', 'mx', 'ne', 'ng', 'nl', 'no', 'nr', 'nu', 'qa', 'pf', 'pk', 'pl', 'pn', 'pt', 're', 'ro', 'ru', 'rw', 'sc', 'se', 'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'td', 'tg', 'tk', 'tm', 'tn', 'to', 'tt', 'ua', 'us', 'vg', 'vn', 'vu', 'ws', 'com']


def get_random_close(sec):
    rand = random.random()
    stri = float(str(rand)[:4])
    return sec + stri


def re_captcha():
    code = input('code:')
    browser.find_element_by_name('PinVerificationForm_pinParam').send_keys(code)
    time.sleep(get_random_close(2))
    browser.find_element_by_name('signin').click()
    time.sleep(get_random_close(1))

    if browser.current_url == 'https://www.linkedin.com/feed/':
        return 0
    else:
        re_captcha()


def login():
    browser.get("http://www.linkedin.com/")
    user = input('user:')
    browser.find_element_by_id('login-email').send_keys(user)
    time.sleep(get_random_close(0))
    password = input('pass:')
    browser.find_element_by_id('login-password').send_keys(password)
    time.sleep(get_random_close(1))
    browser.find_element_by_id('login-submit').send_keys(Keys.RETURN)

    time.sleep(get_random_close(4))
    if browser.current_url == 'https://www.linkedin.com/uas/consumer-email-challenge':
        re_captcha()
    elif browser.current_url != 'http://www.linkedin.com/feed/':
        time.sleep(60)


def get_link():
    element = driver.find_elements_by_class_name('r')

    for links in element:
        linkss = links.find_elements_by_tag_name('a')
        _link = linkss[0].get_attribute('href')
        if 'linkedin.com/in' in _link:
            if 'www' not in _link:
                pos = _link.find('.linkedin')
                _link = "https://www" + _link[pos:]
                link.append(_link)

def get_search_link():
    with open('./search.txt', 'r') as s_f:
        univers = s_f.readlines()
        searches = []
        fore_tag = '"Civil Service Fast Stream" + "'
        after_tag = '" + site:linkedin.com'
        for i in univers:
            searches.append(fore_tag + i[:-1] + after_tag)
    return searches


def search(_search_link):
    global countries
    # n = ''
    # searches = u''
    # while n != ' ':
    #     n = input("强制关键词（如，人名，职位，所属单位等）：")
    #     if n != ' ':
    #         searches = searches + 'intitle:' + n + '+'
    #
    # n = ''
    # while n != ' ':
    #     n = input("弱性关键词（如，参与项目，人际关系，学习经历等）：")
    #     if n != ' ':
    #         searches = searches + '"' + n + '"' + '+'
    #
    # searches += "site:linkedin.com"
    driver.get("https://www.google.com")
    # if driver.current_url[] == 'https://www.google.com/'
    time.sleep(get_random_close(2))
    driver.find_element_by_name('q').send_keys(_search_link)
    time.sleep(get_random_close(1))
    driver.find_element_by_name('btnK').click()
    times = 0
    while len(driver.find_elements_by_id('pnnext')) != 0:
        time.sleep(get_random_close(2))
        get_link()
        driver.find_element_by_id('pnnext').click()
        times += 1

    time.sleep(get_random_close(1))
    get_link()


def read_profile(_link):
    browser.get(_link)
    if browser.current_url[:28] != 'https://www.linkedin.com/in/':
        n = input('wait')
    time.sleep(get_random_close(1))

    time.sleep(get_random_close(1))

    prof = ''
    name = ''
    js = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    time.sleep(get_random_close(0))
    browser.execute_script(js)
    time.sleep(get_random_close(0))
    browser.execute_script(js)

    time.sleep(get_random_close(1))
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "footer-logo"))
        )
        print('10% done!')
        js = "var q=document.documentElement.scrollTop=0"
        browser.execute_script(js)
        time.sleep(1.12)
        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         EC.presence_of_all_elements_located((By.XPATH, '//*[@id="profile-wrapper"]/div/div/div[1]/div[2]/section/div[4]/button'))
        #     )
        #     browser.find_element_by_xpath('//*[@id="profile-wrapper"]/div/div/div[1]/div[2]/section/div[4]/button').click()
        #     time.sleep(get_random_close(1))
        #     print('cliclicli')
        # except Exception as ew:
        #     print('ew')

        js = "var q=document.documentElement.scrollTop=500"
        browser.execute_script(js)

        try:
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "core-rail"))
            )
            print('asdf')
            body = browser.find_element_by_class_name("core-rail")
            print('agag')
            buttons = body.find_elements_by_tag_name('button')
            print(buttons)
            n = 40
            for j in range(2, len(buttons)):
                try:
                    buttons[j].click()
                    time.sleep(get_random_close(1))
                    print('cliclicli')
                    n += 40
                    js = "var q=document.documentElement.scrollTop=" + str(n)
                    browser.execute_script(js)
                    time.sleep(get_random_close(1))

                except Exception as e:
                    js = "var q=document.documentElement.scrollTop=" + str(n)
                    browser.execute_script(js)
                    time.sleep(get_random_close(0))
                    n += 450
                    j -= 1



        except Exception as ew:
            print(ew)


        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(),'查看联系方式')]"))
        #     )
        #     print('found')
        #     js = "var q=document.documentElement.scrollTop=0"
        #     browser.execute_script(js)
        #     time.sleep(get_random_close(0))
        #     browser.find_element_by_xpath("//*[contains(text(),'查看联系方式')]/../..").click()
        #     print(browser.current_url)
        # except Exception as hhh:
        #     print(hhh)

        prof = browser.page_source
        name = browser.title[:-10]
        # element = WebDriverWait(browser, 20).until(
        #     EC.presence_of_element_located((By.ID, "ember1425"))
        # )
        # prof = element.page_source
        byte = bytes(prof, 'utf-8')
        fp = open("./profiles/" + name + ".html", "w+b")  # 打开一个文本文件
        fp.write(byte)  # 写入数据
        fp.close()
        time.sleep(get_random_close(2))
        return True

    except Exception as e:
        return False


if __name__ == '__main__':
    # _proxy = input('proxy:')
    # 127.0.0.1:25378
    # chromeOptions.add_argument("--proxy-server=http://" + _proxy)


    # searches = get_search_link()
    # # searched = open('./searched.txt', 'a')
    # # ssss = searched.readlines()
    # for i in searches:
    #     driver = webdriver.Chrome(chrome_options=chromeOptions)
    #     driver.set_window_size(1366, 768)
    #     try:
    #       search(i)
    #       print(len(link))
    #       ddd = open('./file.txt', 'r')
    #       z = ddd.readlines()
    #       with open('./file.txt', 'a') as f:
    #
    #           ttt = open('./crawed.txt', 'r')
    #           crawed = ttt.readlines()
    #           print(crawed)
    #           for i in range(len(link)):
    #               link[i] = link[i] + '\n'
    #               if (link[i] not in z) and (link[i] not in crawed):
    #                   f.write(link[i])
    #                   z.append(link[i])
    #           ttt.close()
    #       f.close()
    #     except Exception as asdf:
    #         pass
    #     driver.quit()



    with open('./file.txt', 'r') as b:
        now_link = b.readlines()
        print(now_link)
    with open('./file.txt', 'w') as b_w:
        tmp_link = []
        if len(now_link) != 0:
            browser = webdriver.Chrome()
            browser.set_window_size(1366, 768)
            login()
            browser.set_page_load_timeout(100)

            time.sleep(get_random_close(1))
            with open('./crawed.txt', 'a+') as c:
                crawed_link = c.readlines()
                for i in range(len(now_link)):
                    try:
                        now_link[i] = now_link[i].rstrip('\n')
                        if now_link[i] in crawed_link:
                            continue

                        if read_profile(now_link[i]):
                            c.write(now_link[i])
                            c.write('\n')
                            continue

                        b_w.write(now_link[i])
                        b_w.write('\n')
                    except Exception as bbbbb:
                        c.close()
                        continue
                time.sleep(get_random_close(1))
                browser.get('https://www.linkedin.com/m/logout')
                browser.quit()

    b_w.close()
