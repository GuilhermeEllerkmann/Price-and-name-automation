from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

#acess the site
acess_site = webdriver.Firefox()
acess_site.get('https://www.terabyteshop.com.br/pc-gamer/t-gamer')

#gets the price and title data
title_info = acess_site.find_elements(By.XPATH, "//a[@class='prod-name']")
price_info = acess_site.find_elements(By.XPATH, "//div[@class='prod-new-price']")

#creates the excel sheet, and in the sheet, it creates the page where it will receive the data.
workbook = openpyxl.Workbook()
workbook.create_sheet('Products')
sheet_products = workbook['Products']
sheet_products['A1'].value = 'Products'
sheet_products['B1'].value = 'Price'

# It goes through the data that we got from the site and adds it to the Excel sheet.
for text, price in zip(title_info, price_info):
    sheet_products.append((text.text, price.text))
    
#saves the sheet
workbook.save('produtos.xlsx')

