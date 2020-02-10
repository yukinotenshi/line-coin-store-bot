from handler.base import Handler
from appium import webdriver

import os
import time


class StartHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        welcome = driver.find_element_by_id("jp.naver.line.android.registration:id/header")
        return welcome is not None and welcome.text == "Welcome to LINE"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        start_btn = driver.find_element_by_id("jp.naver.line.android.registration:id/next")
        start_btn.click()


class PhoneNumberHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/header')
        return headers is not None and headers.text == "What's the phone number for this device?"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        phone_number_input = driver.find_element_by_id("jp.naver.line.android:id/edit_text")
        phone_number_input.clear()
        phone_number_input.send_keys(os.getenv("LINE_PHONE_NUMBER"))

        driver.hide_keyboard()

        next_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/next')
        next_btn.click()

        time.sleep(3)

        ok_btn = driver.find_element_by_id('jp.naver.line.android:id/common_dialog_ok_btn')
        ok_btn.click()


class VerifyCodeHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/title')
        return headers is not None and headers.text == "Enter verification code"

    def handle(self, sm):
        '''driver: webdriver.Remote = sm.data['driver']
        digit_xpath = '//android.view.View[@content-desc="Verification code"]/android.widget.LinearLayout/android.widget.EditText[{}]'
        code = input('Verification code: ')
        for c in code:
            c = int(c) + 7
            driver.press_keycode(c)

        driver.press_keycode(66)'''
        time.sleep(5)


class HaveAccountPromptHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/header')
        return headers is not None and headers.text == "Already have an account?"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        have_acc_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/transfer_account')
        have_acc_btn.click()


class LoginMethodHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/title')
        return headers is not None and headers.text == "How do you want to log in?"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        email_login_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/use_email_address')
        email_login_btn.click()


class EmailInputHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/title')
        return headers is not None and headers.text == "What's your email address?"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        email_input = driver.find_element_by_id('jp.naver.line.android:id/edit_text')
        email_input.send_keys(os.getenv("LINE_EMAIL"))

        next_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/next')
        next_btn.click()


class PasswordInputHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/title')
        return headers is not None and headers.text == "What's your password?"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        password_input = driver.find_element_by_id('jp.naver.line.android:id/edit_text')
        password_input.send_keys(os.getenv("LINE_PASSWORD"))

        next_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/next')
        next_btn.click()


class LoginHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android.registration:id/header')
        return headers is not None and headers.text.find('Log in as') != -1

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        login_btn = driver.find_element_by_id('jp.naver.line.android.registration:id/log_in')
        login_btn.click()

        sm.state = "DONE"


HANDLERS = [
    StartHandler(),
    PhoneNumberHandler(),
    VerifyCodeHandler(),
    HaveAccountPromptHandler(),
    LoginMethodHandler(),
    EmailInputHandler(),
    PasswordInputHandler(),
    LoginHandler()
]
