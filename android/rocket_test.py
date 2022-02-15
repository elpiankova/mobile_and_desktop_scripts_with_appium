import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


desired_caps = {
    "automationName": "UiAutomator2",
    # "app": Note that this capability is not required for Android if you specify appPackage and appActivity capabilities (see below).
    # "browserName": "Chrome" # For web tests
    'platformName': 'Android',
    'platformVersion': '7.0',
    # "avd": 'Pixel_2_API_30',
    # "UDID": "emulator-5554",
    "UDID": "ZY22DGL6BC",
    'deviceName': 'Android',
    'appPackage': 'ua.raketa.app',
    'appActivity': 'ua.raketa.app.ui.activity.MainActivity',
    "autoGrantPermissions": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Подготовка объектов цепочек действий:
touch_action = TouchAction(driver)
# Обычный ActionChains от selenium тоже успешно работает, но у него не хватает всех необходимых действий
simple_actions = ActionChains(driver)

screen_size = driver.get_window_size()
print(screen_size)
time.sleep(5)

# tap
touch_action.tap(x=522, y=951).wait(100).perform()
# Длинный tap:
touch_action.long_press(x=522, y=951, duration=20).wait(100).perform()
# А этот tap, который
driver.tap([(screen_size["width"]//2, screen_size["height"]//2+50)])


touch_action.press(x=701, y=1325).move_to(x=761, y=1615).release().wait(100).perform()
driver.swipe(start_x=163, start_y=861, end_x=603, end_y=1338, duration=100)

# driver.scroll()
# time.sleep(5)
my_location = driver.find_element(MobileBy.ID, "fab_map_my_location")
touch_action.tap(my_location).perform()
# time.sleep(2)
images = driver.find_elements(MobileBy.CLASS_NAME, "android.widget.ImageView")
# images = WebDriverWait(driver,2).until(presence_of_elements((By.CLASS_NAME, "android.widget.ImageView"), 3))
# print(images)
touch_action.tap(images[2]).wait(5).tap(images[2]).perform()
touch_action.tap(images[2], count=2).perform()
# touch_action.tap(images[2]).perform()
print("End")
# simple_actions.double_click().perform()
