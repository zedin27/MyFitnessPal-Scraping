from config import items
from selenium import webdriver

def get_items(i):
	driver = webdriver.Chrome('./chromedriver')
	driver.get("https://www.myfitnesspal.com/")

if __name__ == '__main__':
	get_items(items)
