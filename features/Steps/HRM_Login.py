import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.pages import orangehrm
from allure_commons.types import AttachmentType


@given(u'launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'Open URL')
def open_url(context):
    context.driver.get('https://www.orangehrm.com/')

@then(u'compare if the URL has been opened')
def get_title(context):
    title_value = orangehrm.title
    a = context.driver.find_element(By.XPATH, title_value).is_displayed()
    if a is True:
        allure.attach(context.driver.get_screenshot_as_png(), name="title failed", attachment_type=AttachmentType.PNG)
        assert False
    else:
        assert True

@then(u'close')
def close_browser(context):
    context.driver.close()
