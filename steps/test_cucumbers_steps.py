import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants

caribu_home = 'https://caribu-dev-firebase.web.app/'

# Scenarios

scenarios('../features/cucumbers.feature')


# Fixtures

@pytest.fixture
def browser():

    path = "/home/ak/PycharmProjects/chromedriver"
    b = webdriver.Chrome(executable_path=path)
    b.implicitly_wait(10)

    yield b
    b.quit()


# Given Steps

@given('the Caribu home page is displayed')
def ddg_home(browser):
    browser.get(caribu_home)


# When Steps

@when(parsers.parse('the user Clicks on sign-in page'))
def sign_in_button(browser):
    browser.find_element_by_link_text('Sign In').click()
    print('caribu')

# Then Steps


@then(parsers.parse('user should be redirected to the sign-in page'))
def sign_in_landing_page(browser):
    current_url=browser.current_url
    assert current_url == 'https://caribu-dev-firebase.web.app/login'


