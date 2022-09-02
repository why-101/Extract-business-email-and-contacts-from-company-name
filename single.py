# importing libraries
import itertools
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import csv
import time
import re
import xlwt

# taking input from user
company = str(input("Please Enter Company Name: "))
path = str(input("Please Enter chromedriver Path: ")
# defining web driver for chrome
s = Service(path)
driver = webdriver.Chrome(service=s)

# searching on Google
company = company.replace(' ', '+')
driver.get('https:www.google.com/search?q=' + company)
time.sleep(1)

# clicking on first result
driver.find_element(By.XPATH, "//div[@class='g']//div[@class='yuRUbf']").click()

# reading and downloading all the content from page
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# making list of elements from above
l = []
for a in soup.findAll('a', href=True):
    c = (a['href'])
    ls = c
    l.append(str(ls))

# extracting only data
result = []
char = ['@', '91']

for i in l:
    for j in char:
        if re.search(j, i):
            result.append(i)

book = xlwt.Workbook()
sheet = book.add_sheet("Sheet1")
for i in range(len(result)):
    if len(i) < 100:
        sheet.write(i, 0, result[i])
book.save("list.xls")


# open file in write mode
file = open("contact.txt", "w")

# write results to file
for i in result:
    file.write(str(i) + "\n")
file.close()

# closing browser
driver.quit()

# ANCHOR TEXT

           
print("Thank you for using MY SCRIPT")
