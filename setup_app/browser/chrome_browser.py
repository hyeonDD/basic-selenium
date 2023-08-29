from selenium import webdriver

from setup_app.browser.base import BaseBrowser

driver = webdriver.Chrome()

chrome_browser = BaseBrowser(driver=driver)
