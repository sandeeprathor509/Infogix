from behave import *
from selenium import webdriver
from selenium.common.exceptions import *
import time


@given('Launch the git page')
def brwoser_launch(context):
    context.driver = webdriver.Firefox(
        executable_path=r'/home/ubuntutesting/PycharmProjects/GitTest/drivers/geckodriver')
    context.driver.get('https://github.com/')
    accept_pop = context.driver.find_element_by_xpath("/html/body/div[8]/div/div/div/div[1]/div/div/button[1]")
    accept_pop.click()


@then('User will be navigate to the login page')
def login_page(context):
    dropdown = context.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/button")
    dropdown.click()
    sign_in = context.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
    sign_in.click()


@then('Verify the username and password field mandatory fields')
def mandatory_fields(context):
    sign_button = context.driver.find_element_by_xpath("//input[@name='commit']")
    sign_button.click()
    mandatory_msg = context.driver.find_element_by_xpath("//div[contains(@class,'container-lg px-2')]").text
    text = "Incorrect username or password."
    assert mandatory_msg == text


@then('Close the browser')
def close_browser(context):
    context.driver.close()
