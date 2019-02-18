import requests, time
from settings import *
from selenium import webdriver
from requests.auth import HTTPBasicAuth
import re

def run():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get("http://%s/login"%IP)
    browser.find_element_by_id("username").send_keys(GITSTAR_NAME)
    browser.find_element_by_id("password").send_keys(GITSTAR_PASSWORD)
    browser.find_element_by_css_selector(".btn.btn-default").click()
    res = re.findall(r'href="https://github.com/(.*?)">', browser.page_source)[:-6]
    if "cckuailong/colorsys-go" not in res:
        res.append(["cckuailong/colorsys-go", "cckuailong/Shyvana"])
    AUTH = HTTPBasicAuth(GIT_NAME, GIT_PASSWORD)
    cnt = 1
    print ("Start Star")
    for url in res:
        try:
            requests.put("https://api.github.com/user/starred/" + url
                           , headers={'Content-Length': '0'}
                           , auth=AUTH)
            print ("Stared %d" % cnt)
            cnt += 1
        except:
            pass
        time.sleep(10)

    browser.find_element_by_id("update").click()
    time.sleep(20)
    browser.close()


if __name__ == "__main__":
    run()