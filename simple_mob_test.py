# To successfully run this test you should have connected android device
# This script will just open Calculator Android app on your android device

import time
from appium import webdriver


desired_caps = {
    "automationName": "UiAutomator2",
    # "app": # Note that this capability is not required for Android if you specify appPackage and
             # appActivity capabilities (see below).
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

driver.quit()
