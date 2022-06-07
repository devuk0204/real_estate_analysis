from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

url = "https://www.ministop.co.kr/MiniStopHomePage/page/store/store.do"
driver = webdriver.Chrome('../chromedriver')
driver.get(url)

time.sleep(0.2)
select_sido = Select(driver.find_element_by_xpath('//*[@id=\"area1\"]'))
select_sido.select_by_value('16')

driver.find_element_by_xpath('//*[@id=\"section\"]/div[3]/div/div[2]/div[2]/div[1]/a').click()
csv_list = []
time.sleep(0.1)

i = 0
while i < 500 :
    try :
        csv_list.append(driver.find_element_by_xpath('//*[@id=\"section\"]/div[3]/div/div[2]/div[2]/div[1]/ul/li[' + str(i+1) + ']').text)
    except :
        i = 500
    else :
        print(str(i) + ' ' +csv_list[i])
        i += 1    
        

with open('../data/ministop_csv_location.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(csv_list)
driver.close()