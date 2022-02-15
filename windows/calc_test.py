from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
# "Microsoft.WindowsCalculator_10.2103.8.0_x64__8wekyb3d8bbwe"

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723',
                          desired_capabilities=desired_caps)

window = driver.find_element(MobileBy.NAME, 'Calculator')
window.find_element(MobileBy.NAME, "Clear").click()
# driver.find_element_by_name("Seven").click()
driver.find_element(MobileBy.ACCESSIBILITY_ID, "num3Button").click()
# result_el = driver.find_element_by_accessibility_id("CalculatorResults")
result_el = driver.find_element(MobileBy.XPATH, "//Text[@AutomationId=\"CalculatorResults\"]")

assert result_el.text == "Display is 3"
print(result_el.text)
print(result_el.get_attribute("ControlType"))

actions = TouchAction(driver)
actions.tap(driver.find_element(MobileBy.NAME, "Seven"))
actions.long_press()
actions.perform()

# driver.quit()
