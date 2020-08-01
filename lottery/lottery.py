# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:32:57 2020

@author: 朱瑋民
"""
import time
import pandas as pd
import numpy as np
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys#鍵盤的操作
from selenium.webdriver.common.action_chains import ActionChains#滑鼠的操作
from bs4 import BeautifulSoup
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool
from bokeh.models.widgets import Dropdown, Tabs, Panel
from bokeh.layouts import column
import csv

URL = "https://www.pilio.idv.tw/lto/list.asp"
driver = None
def start_driver():
    global driver
    print("啟動 WebDriver...")
    driver = webdriver.Chrome("./chromedriver")
    driver.implicitly_wait(5)
    
def close_driver():
    global driver
    driver.quit()
    print("關閉 WebDriver...")
def get_page(url):
    global driver
    print("取得網頁...")
    driver.get(url)
    time.sleep(2)
def search():
    global driver   
    #time.sleep(1)
    search=driver.find_elements_by_xpath('//*[@id="Button1"]')
    search[0].click()


if __name__ == "__main__":
    number6=[]
    number1=[]
    
    start_driver()
    get_page(URL)
    #soup=BeautifulSoup(driver.page_source,"lxml")
    #table1=soup.select_one("#main > div > table:nth-child(2)") 
    #df=pd.read_html(str(table1))
    
    #main > div > table:nth-child(2)
    #ltotable
    #df[0].to_csv("號碼.csv",encoding='utf-8-sig',index=False, header=False)
    #fp=pd.read_csv("號碼.csv")
    for k in range(9):
        special=driver.find_elements_by_xpath('//*[@id="main"]/div/table[1]/tbody/tr[{}]/td[2]'.format(k+2))
        eight=driver.find_elements_by_xpath('//*[@id="main"]/div/table[1]/tbody/tr[{}]/td[3]'.format(k+2))
        string1=special[0].text
        string2=eight[0].text
        ss1=list(string1.split(", "))
        ss2=list(string2.split(", "))
        final1=list(map(int, ss1))
        final2=list(map(int, ss2))
        number6.append(final2)  #用()即可以解決添加陣列的問題
        number1.append(final1)

    for i in range(400):
        search()
    for j in range(1714):
        special=driver.find_elements_by_xpath('//*[@id="ltotable"]/tbody/tr[{}]/td[3]'.format(j+1))
        eight=driver.find_elements_by_xpath('//*[@id="ltotable"]/tbody/tr[{}]/td[2]'.format(j+1))
        string1=special[0].text
        string2=eight[0].text
        ss1=list(string1.split(", "))
        ss2=list(string2.split(", "))
        final1=list(map(int, ss1))
        final2=list(map(int, ss2))
        number6.append(final2)  #用()即可以解決添加陣列的問題
        number1.append(final1)
    print(number6)
    result=pd.DataFrame()
    result["six_number"]=number6
    result["one_number"]=number1
    result.to_csv('resulttt.csv',encoding='utf-8-sig')
    close_driver()









