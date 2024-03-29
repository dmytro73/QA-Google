import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("order food near me")
    g.send_Keys('webdriver');
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Search in Google"))
