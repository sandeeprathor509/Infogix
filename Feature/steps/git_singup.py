from behave import *
from selenium.common.exceptions import *


@then('Click on the signup button')
def sign_up(context):
    signup_btn = context.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/a")
    signup_btn.click()


@then('Verify the Join GitHub text on the signup page')
def git_hub_txt(context):
    join_txt = context.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[1]/div")
    text = "Join GitHub"
    assert text in join_txt.text


@then('Verify the presence Create account button')
def create_acnt_btn(context):
    try:
        crt_act_btn = context.driver.find_element_by_xpath("//button[@id='signup_button']")
    except NoSuchElementException:
        return False
    return True
