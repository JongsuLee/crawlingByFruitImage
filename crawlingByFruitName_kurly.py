from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


def crawl(item):
    driver = webdriver.Chrome(ChromeDriverManager().install())

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
        weight = 1
        for x in spans[2].text.split():
            if 'kg' in x:
                weight = float(x.replace('kg', '')) * 10
            elif 'g' in x:
                weight = float(x.replace('g', '')) / 100

        if '%' in spans[3].text:
            price = int(spans[4].text.split()[-2].replace(',', ''))
        else:
            price = int(spans[3].text.split()[-2].replace(',', ''))
        
        unitPrice = str(int(price / weight))

        if len(unitPrice) > 3:
            result = ""

            for j in range(len(unitPrice)):
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