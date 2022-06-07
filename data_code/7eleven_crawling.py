from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

url = "https://www.7-eleven.co.kr/"
driver = webdriver.Chrome('../chromedriver')
driver.get(url)
time.sleep(0.3)

driver.find_element_by_xpath('//*[@id="header"]/div/div/div[1]/a[1]').click()
time.sleep(0.5)

select_sido = Select(driver.find_element_by_id('storeLaySido'))
select_sido.select_by_index(8)
time.sleep(0.2)

driver.find_element_by_id('storeButton1').click()
time.sleep(0.3)

csv_list = []

i = 0
while i < 800 :
    try :
        csv_list.append(driver.find_element_by_xpath('//*[@id=\"storeForm\"]/div[1]/div[2]/ul/li[' + str(i+1) + ']/a/span[2]').text)
    except :
        i = 800
    else :
        print(csv_list[len(csv_list)-1])
        i += 1
        
with open('../data/7eleven_csv_location.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(csv_list)
driver.close()
