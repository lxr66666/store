from appium import webdriver
import time
# import datetime



server = "http://localhost:4723/wd/hub"
param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,param)

time.sleep(5)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()

time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
for i in range(10):
# while True:

    driver.swipe(500, 1200, 500, 400, 300)
    time.sleep(3)

    # currenttime = datetime.datetime.now()

    # if str(currenttime)[:-7] == '2021-07-05 16:50:00':
    #     break


driver.quit()