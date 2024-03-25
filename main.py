import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

desired_caps = UiAutomator2Options()
desired_caps.device = "Android12"
desired_caps.app = os.path.abspath("apps/app.apk")
desired_caps.platformName = "Android"

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="intro-screen/sign-up-button")
el1.click()
