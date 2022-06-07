from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

driver = webdriver.Chrome("../chromedriver")

driver.get("http://gs25.gsretail.com/gscvs/ko/store-services/locations")

select_location = Select(driver.find_element_by_id('stb1'))
select_location.select_by_value('26')

search_button = driver.find_element_by_css_selector('#searchButton')
search_button.click()

address_list = []

time.sleep(1)



for i in range(176) :
    time.sleep(1)
    
    for j in range(5) :
        try :
            address_list.append(driver.find_element_by_xpath('//*[@id=\"storeInfoList\"]/tr[' + str(j+1) + ']/td[2]/a').text)
        except :
            print('end')
            
    print(address_list[len(address_list)-5:len(address_list)-1])
    
    
    next_button = driver.find_element_by_css_selector('#pagingTagBox > a.next')
    next_button.click()   
        

with open('gs_csv_location.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(address_list)
#driver.close()