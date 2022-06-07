from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

url = "https://emart24.co.kr/introduce2/findBranch.asp"
driver = webdriver.Chrome('../chromedriver')
driver.get(url)

select_sido = Select(driver.find_element_by_id('stplacesido'))
select_sido.select_by_index(8)

driver.execute_script('javascript:goPage(1);')
time.sleep(0.3)

csv_list = []

i = 0
while i < 75 :
    time.sleep(0.2)
    j = 0
    while j < 5 :
        try :
            csv_list.append(driver.find_element_by_xpath('//*[@id=\"skipCont\"]/div[2]/div[3]/table/tbody/tr['+ str(j+1) + ']/td[2]/p[1]').text)
        except :
            j = 5
        else :
            print(csv_list[len(csv_list)-1])
            j += 1
        
    try :
        driver.find_element_by_xpath('//*[@id=\"skipCont\"]/div[2]/div[3]/div/a[13]/img').click()
    except :
        driver.find_element_by_xpath('//*[@id=\"skipCont\"]/div[2]/div[3]/div/a[8]/img').click()
    i += 1

with open('../data/emart24_csv_location.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(csv_list)
driver.close()