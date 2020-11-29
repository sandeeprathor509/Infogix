from behave import *


@then('Click on forgot password')
def fgt_passwd(context):
    fgt_pswd = context.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/label[2]/a")
    fgt_pswd.click()


@then('Enter the m.ie in the username field')
def enter_usrname(context):
    email = context.driver.find_element_by_xpath("//*[@id='email_field']")
    email.send_keys("m.ie")


@then('verify the text after entering the wrong email')
def verify_msg(context):
    rst_email = context.driver.find_element_by_xpath("//input[@name='commit']")
    rst_email.click()
    text = 'That address is not a'
    wrn_msg = context.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[2]/div/div")
    assert text in wrn_msg.text


@then('Verify the text after entering nothing in email')
def empty_msg(context):
    rst_email = context.driver.find_element_by_xpath("//input[@name='commit']")
    rst_email.click()
    text = 'That address is not a'
    wrn_msg = context.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[2]/div/div")
    assert text in wrn_msg.text
