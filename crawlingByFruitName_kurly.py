from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import os


def crawl(item):
    print('start')
    print(f'pwd: {os.listdir(".")}')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    service = Service('chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    kurly = 'https://www.kurly.com/main'

    driver.get(kurly)

    toSearch = driver.find_element(By.TAG_NAME, 'input')
    toSearch.send_keys(item, Keys.ENTER)

    time.sleep(1)
    productsFrame = driver.find_elements(By.CLASS_NAME, 'css-1xyd46f')
    spans = productsFrame[0].find_elements(By.TAG_NAME, 'span')

    kurly_products = {}

    for i, frame in enumerate(productsFrame[:5]):
        img = frame.find_element(By.TAG_NAME, 'img').get_attribute('src')
        spans = frame.find_elements(By.TAG_NAME, 'span')
        weight = None
        for x in spans[2].text.split():
            if 'kg' in x:
                weight = float(x.replace('kg', '')) * 10
                break
            elif 'g' in x:
                weight = float(x.replace('g', '')) / 100
                break

        price = int(frame.find_element(By.CLASS_NAME, 'sales-price').text.split()[0].replace(',', ''))
        
        if weight:
            unitPrice = str(int(price / weight))
        else:
            unitPrice = ""

        if len(unitPrice) > 3:
            result = ""

            for j in range(1, len(unitPrice) + 1):
                if j % 3 == 1 and j // 3 > 0:
                    result = unitPrice[-1 * j] + ','  + result
                else:
                    result = unitPrice[-1 * j] + result
            
            unitPrice = result

        kurly_products[i + 1] = {'img': img,
                                 'url': frame.get_attribute('href'),
                                 'title': spans[2].text,
                                 'price': str(price) + " 원",
                                 'unitPrice': unitPrice + '원/100g'}


    return kurly_products
