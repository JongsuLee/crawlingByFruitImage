from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import re

def crawl(item):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.gmarket.co.kr/')

    toSearch = driver.find_element(By.TAG_NAME, 'input')
    toSearch.send_keys(item, Keys.ENTER)
    time.sleep(1)

    toSort = driver.find_element(By.CLASS_NAME, 'list__depth')
    toSorts = toSort.find_elements(By.TAG_NAME, 'span')

    for x in toSorts:
        if x.text == '신선식품':
            toClick = x

    if globals().get('toClick', None):
        ActionChains(driver).click(toClick).perform()
        time.sleep(1)

    gmarket_products = {}
    num_filter = re.compile('[^0-9.]')

    productFrame = driver.find_elements(By.CLASS_NAME, 'box__component-itemcard')

    for i, frame in enumerate(productFrame[:5]):
        img = frame.find_element(By.TAG_NAME, 'img').get_attribute('src')
        url = frame.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
        title = frame.find_elements(By.CLASS_NAME, 'text__item')[0].text
        textPrice = frame.find_element(By.TAG_NAME, 'strong').text
        price = textPrice

        if ',' in price:
            price = int(price.replace(',', ''))
        else:
            price = int(price)
        
        weight = None
        for x in title.split():
            if 'kg' in x:
                weight = num_filter.sub('', x.split()[0])
                weight = float(weight[0]) * 10
                break
            elif 'g' in x:
                weight = num_filter.sub('', x.split()[0])
                weight = float(weight) / 10
                break
        
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
        
        gmarket_products[i + 1] = {'img': img,
                                   'url': url,
                                   'title': title,
                                   'price': textPrice + ' 원',
                                   'unitPrice': unitPrice + '원/100g'}

    

    return gmarket_products