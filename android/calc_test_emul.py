# To successfully run this test you should switch on android emulator device
# This script will just open Calculator Android app on your android device

import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains

desired_caps = {
    "automationName": "UiAutomator2",
    # "app": For path to .apk file.
    # "browserName": "Chrome" # For web tests
    "platformName": "Android",
    "platformVersion": "11",
    # "avd": 'Nexus_6_API_27',
    "avd": "Pixel_2_API_30",
    # "UDID": "ZY22DGL6BC",
    "deviceName": "Android",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element(MobileBy.ID, "digit_9").click()
driver.find_element(MobileBy.ID, "op_add").click()
driver.find_element(MobileBy.ID, "digit_9").click()
driver.find_element(MobileBy.ACCESSIBILITY_ID, "equals").click()
time.sleep(1)
result = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/result_final")

assert result.text == "18"


advance = driver.find_element(MobileBy.CLASS_NAME, "androidx.slidingpanelayout.widget.SlidingPaneLayout")
print(advance.location)
print(advance.size)
# advance.click()

# actions = TouchAction(driver)
# actions.tap()
# actions.press(advance,  advance.size["width"]-5, advance.size["height"]//2)
# actions.move_to(advance, advance.size["width"]-5, advance.size["height"]//2)
# actions.release()
# actions.perform()

actions = ActionChains(driver)
actions.move_to_element_with_offset(advance,  advance.size["width"]-5, advance.size["height"]//2)
actions.click_and_hold()
actions.move_by_offset(advance.size["width"]-5, advance.size["height"]//2)
actions.release()
actions.perform()

driver.quit()
