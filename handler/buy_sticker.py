from handler.base import Handler
from appium import webdriver

import time


'''class StartHandler(Handler):
    def could_handle(self, sm):
        print(sm.data['first_time'])
        return sm.data['first_time']

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        more_btn = driver.find_element_by_xpath('(//android.view.View[@content-desc="@{bottomNavigationBarButtonViewModel.contentDescription"])[5]/android.view.View')
        more_btn.click()

        sm.data['first_time'] = False


class StickerShopHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Sticker Shop"]/android.widget.RelativeLayout')
        return btn is not None

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Sticker Shop"]/android.widget.RelativeLayout')
        btn.click()

        time.sleep(7)


class SearchHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Sticker Shop"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        btn = driver.find_element_by_id('jp.naver.line.android:id/header_left_button_img')
        btn.click()


class StickerInputHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Search"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        id_input = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText')
        id_input.click()
        for _ in range(30):
            driver.press_keycode(67)

        id_input.send_keys(sm.data["sticker_name"])
        driver.press_keycode(66)

        time.sleep(3)
        creator_btn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.ListView/android.view.View[2]')
        creator_btn.click()

        time.sleep(3)
        sticker_name = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View[2]/android.view.View[2]')
        sm.data['sticker_name'] = sticker_name
        print(sticker_name)
        sticker_name.click()
'''


class StartIntentHandler(Handler):
    def could_handle(self, sm):
        return sm.data['first_time']

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        driver.execute_script("mobile:deepLink", {
            "url": sm.data['sticker_link'],
            "package": "jp.naver.line.android"
        })
        sm.data['first_time'] = False


class BuyStickerHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Sticker set info"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        gift_btn = driver.find_element_by_id('jp.naver.line.android:id/shop_detail_present_button')
        gift_btn.click()


class ChooseFriendHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        header = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return header is not None and header.text == "Choose friends"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        search = driver.find_element_by_id('jp.naver.line.android:id/searchbar_input_text')
        search.clear()
        search.send_keys(sm.data["target"])
        driver.press_keycode(66)

        time.sleep(5)

        friend_name = driver.find_element_by_id('jp.naver.line.android:id/widget_friend_row_name')
        sm.data['recipient'] = friend_name.text

        select_friend = driver.find_element_by_id('jp.naver.line.android:id/widget_friend_row_checkbox')
        select_friend.click()

        next_btn = driver.find_element_by_id('jp.naver.line.android:id/header_button_text')
        next_btn.click()


class GiftHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        headers = driver.find_element_by_id('jp.naver.line.android:id/header_title')
        return headers is not None and headers.text == "Gift details"

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        gift_btn = driver.find_element_by_id('jp.naver.line.android:id/present_purchase_button')
        gift_btn.click()

        time.sleep(3)

        ok_btn = driver.find_element_by_id('jp.naver.line.android:id/common_dialog_ok_btn')
        ok_btn.click()

        time.sleep(5)
        driver.press_keycode(4)

        sm.state = "DONE"


HANDLERS = [
    StartIntentHandler(),
    BuyStickerHandler(),
    ChooseFriendHandler(),
    GiftHandler()
]
