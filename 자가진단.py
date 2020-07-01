from selenium import webdriver

import time

school = ""
name   = ""
born   = ""

driver = webdriver.Chrome('C:/chromedriver.exe')
 
driver.get("https://eduro.sen.go.kr/stv_cvd_co00_002.do")  

driver.find_element_by_name("schulNm").send_keys(school)

driver.find_element_by_name("pName").clear()
driver.find_element_by_name("pName").send_keys(name)

driver.find_element_by_name("frnoRidno").clear()
driver.find_element_by_name("frnoRidno").send_keys(born)


driver.find_element_by_id("btnConfirm").click()

time.sleep(1)

for table in driver.find_elements_by_class_name("tables_board"):    
    table.find_element_by_css_selector("tbody > tr:nth-child(2) > td > span > label:nth-child(1)").click()

  
driver.find_element_by_id("btnConfirm").click()
