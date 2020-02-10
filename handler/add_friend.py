from handler.base import Handler
from appium import webdriver

import time


class StartHandler(Handler):
    def could_handle(self, sm):
        return sm.data['first_time']

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        friends_btn = driver.find_element_by_xpath('(//android.view.View[@content-desc="@{bottomNavigationBarButtonViewModel.contentDescription"])[1]/android.view.View')
        friends_btn.click()

        sm.data['first_time'] = False


class AddFriendHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Add friends button"]/android.widget.ImageView')
        return btn is not None

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="Add friends button"]/android.widget.ImageView')
        btn.click()


class SearchHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Add friends"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[4]')
        btn.click()


class IDInputHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Friend search"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        id_input = driver.find_element_by_id('jp.naver.line.android:id/addfriend_by_userinfo_search_text')
        id_input.clear()
        id_input.send_keys("blxcklisted")

        search_btn = driver.find_element_by_id('jp.naver.line.android:id/addfriend_by_userid_search_button_image')
        search_btn.click()


class NotFoundHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView')
        return headers is not None and headers.text == "User not found."

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        back_btn = driver.find_element_by_id('jp.naver.line.android:id/header_up_button')
        back_btn.click()

        driver.press_keycode(4)

        sm.state = "DONE"


class FinalHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        add_btn = driver.find_element_by_id('jp.naver.line.android:id/addfriend_add_button')
        return add_btn is not None

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']

        name = driver.find_element_by_id('jp.naver.line.android:id/addfriend_name')
        print(name.text)
        sm.data['name'] = name.text

        add_btn = driver.find_element_by_id('jp.naver.line.android:id/addfriend_add_button')
        if add_btn.text == "Add":
            add_btn.click()

        driver.press_keycode(4)
        time.sleep(2)
        driver.press_keycode(4)

        sm.state = "DONE"


HANDLERS = [
    StartHandler(),
    AddFriendHandler(),
    SearchHandler(),
    NotFoundHandler(),
    FinalHandler(),
    IDInputHandler()
]
