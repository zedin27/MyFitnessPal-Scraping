from config import items
import requests
from selenium import webdriver
import time
import re

def get_items(i):
	#dict stores item names with their protein value
	dict = {}
	driver = webdriver.Chrome("./chromedriver")

	for i in items:
		driver.get("https://www.myfitnesspal.com/")
		driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[2]/form/input').send_keys(i)
		search_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[2]/form/button')
		search_button.click()
		item_html = requests.get(driver.current_url)
		html_file = open('html.txt', 'w')
		html_file.write(item_html.text)
		html_file = open('html.txt')

		for j in html_file.readlines():
			match = re.search('Protein: (\d+)', j)
			if match:
				dict[i] = match.group()
	# print(dict)

if __name__ == "__main__":
	get_items(items)
