from abc import ABC, abstractclassmethod

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from setup_app.setting.config import settings

TIMEOUT = settings.TIMEOUT


class ABCBrowser(ABC):
    """Browser 인터페이스"""
    @abstractclassmethod
    def _wait_for_element(self, *, element: str):
        """ 요소를 기다리는 메서드 """

    @abstractclassmethod
    def move_url(self, url: str):
        """ 요소 클릭 메서드 """

    @abstractclassmethod
    def click_element(self, *, element: str, option: str):
        """ 요소 클릭 메서드 """

    @abstractclassmethod
    def input_text_filed(self, *, element: str, option: str):
        """ 텍스트필드 채우기 메서드 """

    @abstractclassmethod
    def select_check_box(self, *, element: str, option: str):
        """ 체크박스 선택 메서드 """

    @abstractclassmethod
    def click_link_tag(self, *, element: str, option: str):
        """ link 태그 선택 메서드 """


class BaseBrowser(ABCBrowser):
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.options = {
            'id': By.ID,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'name': By.NAME,
            'tag_name': By.TAG_NAME,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }

    def _wait_for_element(self, *, element: str, option: str) -> WebElement:
        option = self.options[option]
        result_element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located((option, element))
        )
        return result_element

    def move_url(self, url: str):
        self.driver.get(url)

    def click_element(self, *, element: str, option: str):
        result_element = self._wait_for_element(
            element=element, option=option)
        result_element.click()

    def input_text_filed(self, *, element: str, text: str, option: str):
        result_element = self._wait_for_element(
            element=element, option=option)

        actions = webdriver.ActionChains(self.driver).send_keys_to_element(
            result_element, text).send_keys(Keys.ENTER)
        actions.perform()

    # TODO
    def select_check_box(self, *, element: str, option: str):
        pass

    def click_link_tag(self, *, element: str, option: str):
        result_element = self._wait_for_element(
            element=element, option=option)
        result_element.click()
