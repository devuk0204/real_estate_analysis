from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

driver = webdriver.Chrome("../chromedriver")

driver.get("https://cu.bgfretail.com/store/list.do?category=store")
time.sleep(0.05)

select_sido = Select(driver.find_element_by_id('sido'))
select_sido.select_by_value('부산광역시')

select_gu = Select(driver.find_element_by_id('Gugun'))
csv_list = []
for i in range(16) :
    select_gu.select_by_index(i+1)
    select_dong = Select(driver.find_element_by_id('Dong'))
    j = 0
    while j < 250 :
        try :
            select_dong.select_by_index(j+1)
        except :
            print('e')
            j = 250
        else :
            j += 1
            select_button = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/input[1]')
            driver.execute_script('usertsearchList(1); return false;')
            time.sleep(0.1)
            m = 0
            while m < 10 :
                h = 0
                while h < 5 :
                    try :
                        csv_list.append(driver.find_element_by_xpath('//*[@id=\"result_search\"]/div[2]/div[1]/table/tbody/tr[' + str(h+1) + ']/td[2]/div/address/a').text)
                    except :
                            print('e')
                            h = 5
                            m = 10
                    else :
                        h += 1
                    time.sleep(0.1)
                driver.execute_script('newsPage(\'' + str(m+2) + '\'); return false;')
                m += 1
            print(str(i) + ' ' + str(j))


with open('../data/cu_csv_location.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(csv_list)
driver.close()