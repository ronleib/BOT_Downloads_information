from selenium import webdriver
from __library import PATH


def i_Url(url):
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    return driver
