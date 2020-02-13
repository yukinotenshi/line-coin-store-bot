from handler.add_friend import *
from appium import webdriver


class OpenChatHandler(Handler):
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
        if add_btn.text == "Chat":
            add_btn.click()


class ChatMenuHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        menu_btn = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Menu button"]/android.widget.ImageView')
        return menu_btn is not None

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        menu_btn = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Menu button"]/android.widget.ImageView')
        menu_btn.click()


class BlockHandler(Handler):
    def could_handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        block_btn = driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Block"]/android.widget.TextView')
        return block_btn is not None

    def handle(self, sm):
        driver: webdriver.Remote = sm.data['driver']
        block_btn = driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@content-desc="Block"]/android.widget.TextView')
        block_btn.click()

        driver.press_keycode(4)
        time.sleep(2)
        driver.press_keycode(4)

        sm.status = "DONE"


HANDLERS = [
    StartHandler(),
    AddFriendHandler(),
    SearchHandler(),
    NotFoundHandler(),
    OpenChatHandler(),
    IDInputHandler(),
    ChatMenuHandler(),
    BlockHandler()
]
