from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
URL = 'https://yandex.ru/images/'
options = Options()

options.set_preference("general.useragent.override", f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0")

def check_exists_by_css(driver, css):
    try:
        driver.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(driver, xpath):
    try:
        driver.find_element(By.CLASS_NAME, xpath)
    except NoSuchElementException:
        return False
    return True

def get_content(line):
    start = time.time()
    print('Start of receiving information...')
    options.headless = True
    url_photo = line
    driver = webdriver.Firefox('/home/rabbit/Project/',options=options)
    driver.get(URL)
    try:
        time.sleep(1.35)
        driver.find_element(By.CSS_SELECTOR, 'button.button2').click()
        time.sleep(0.26)
        driver.find_element(By.CLASS_NAME, 'Textinput-Control').send_keys(url_photo)
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'button.Button2:nth-child(2)').click()
        time.sleep(2.5)
        count_urls = len(driver.find_elements(By.CLASS_NAME,'CbirSites-Items')[0].find_elements(By.CLASS_NAME,'CbirSites-Item'))
        print(count_urls)
        for count in range(0,count_urls):
            print(driver.find_elements(By.CLASS_NAME,'CbirSites-Items')[0].find_elements(By.CLASS_NAME,'CbirSites-Item')[count].find_elements(By.CLASS_NAME, 'CbirSites-ItemInfo')[0].find_elements(By.CLASS_NAME, 'CbirSites-ItemTitle')[0].text)
        if check_exists_by_class_name(driver, 'CbirObjectResponse') == True:
            print('1')
            elementlis = driver.find_elements(By.CLASS_NAME,'CbirObjectResponse-Content')
            if check_exists_by_css(driver,'.CbirObjectResponse-Subtitle'):
                sight = driver.find_element(By.CSS_SELECTOR, '.CbirObjectResponse-Subtitle').text
            else:
                sight = ''
            description = elementlis[0].find_element(By.CLASS_NAME, 'CbirObjectResponse-Description').text
            print(driver.find_element(By.CLASS_NAME,'CbirObjectResponse-Title').text + '\n'+ sight + '\n' + description)
        if check_exists_by_css(driver ,'div.Tags:nth-child(2) > div:nth-child(1)') == True:
            print('2')
            if check_exists_by_css(driver,'button.Button2:nth-child(5)') == True:
                driver.find_element(By.CSS_SELECTOR, 'button.Button2:nth-child(5)').click()
            elif check_exists_by_css(driver,'button.Button2:nth-child(6)') == True:
                driver.find_element(By.CSS_SELECTOR, 'button.Button2:nth-child(6)').click()
            parentelement = driver.find_element(By.CSS_SELECTOR,'div.Tags:nth-child(2) > div:nth-child(1)')
            elementlist = parentelement.find_elements(By.CLASS_NAME, 'Button2-Text')
            for element in elementlist:
                print(element.text)
        driver.quit()
    except NoSuchElementException:
        print(driver.find_element(By.CSS_SELECTOR, 'a.Link_view_captcha:nth-child(1)'))
        href = driver.find_element(By.CSS_SELECTOR, '.AdvancedCaptcha-Image').get_attribute('src')
        print(href)
