# To successfully run this test you should have connected android device
# This script will just open Calculator Android app on your android device

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

desired_caps = {
    "automationName": "UiAutomator2",
    # "app": Note that this capability is not required for Android if you specify appPackage and appActivity capabilities (see below).
    # "browserName": "Chrome" # For web tests
    "platformName": "Android",
    "platformVersion": "11",
    "UDID": "ZY22DGL6BC",
    "deviceName": "Android",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

# advance = driver.find_element_by_class_name("androidx.slidingpanelayout.widget.SlidingPaneLayout")
# driver.swipe(
#     advance.size["width"]-5,
#     advance.location["y"] + advance.size["height"]//2,
#     10,
#     advance.location["y"] + advance.size["height"]//2
# )

el1 = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/digit_9")
el1.click()
el2 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "сложить")
el2.click()
el3 = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/digit_5")
el3.click()
el4 = driver.find_element(MobileBy.ACCESSIBILITY_ID, "равно")
el4.click()
el5 = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/result_final")
assert el5.text == "14"
# TouchAction(driver).press(x=548, y=554).move_to(x=540, y=830).release().perform()


driver.find_element(MobileBy.ID, "digit_9").click()
driver.find_element(MobileBy.ID, "op_add").click()
driver.find_element(MobileBy.ID, "digit_9").click()
# driver.find_element(By., "=").click()
# driver.find_element_by_accessibility_id("равно").click()
driver.find_element(MobileBy.ACCESSIBILITY_ID, "равно").click()
result = driver.find_element(MobileBy.ID, "result_final")
assert result.text == "18"


advance = driver.find_element(MobileBy.ID, "com.google.android.calculator:id/drag_handle_view")
print(advance.location)
print(advance.size)
# advance.click()
actions = TouchAction(driver)
actions.tap()
actions.press(advance,  advance.size["width"]-1, advance.size["height"]//2)
actions.move_to(advance, 0, 500)
actions.release()
actions.perform()
# TouchAction(driver)   .press(x=542, y=793)   .move_to(x=542, y=1590)   .release()   .perform()

# driver.tap()
driver.swipe(
    advance.size["width"]-5,
    advance.location["y"] + advance.size["height"]//2,
    10,
    advance.location["y"] + advance.size["height"]//2
)

driver.quit()
# # adb shell dumpsys window | find "mCurrentFocus"




