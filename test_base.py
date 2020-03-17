from selenium import webdriver
import pytest
import math


class TestBase:

    @pytest.fixture
    def browser(self) -> webdriver.Chrome:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        yield browser
        browser.quit()

    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
