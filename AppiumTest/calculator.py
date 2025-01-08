from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

class calculator:

    
    desired_caps = {
            'platformName': 'Android',
            'platformVersion': '12',
            'deviceName': 'PGAM10',
            'appPackage': 'com.ibox.calculators',
            'appActivity': '.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'

        }


    def __init__(self):
        self.driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=UiAutomator2Options().load_capabilities(self.desired_caps))




    def Simplecalculate(self,op,num1=None,num2=None):

        self.driver.implicitly_wait(10)


        # driver.find_element(AppiumBy.CLASS_NAME,'android.view.View').click()
        sleep(10)
            #完成一个 计算 3+9 ，结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过

        agree=self.driver.find_elements(AppiumBy.ID,'user_privacy_ok')

        if agree:

            agree.click()

        if num1 is not None:
            num1=self.driver.find_element(AppiumBy.ID,'digit'+str(num1))
            num1.click()

        if op=='+':
            self.driver.find_element(AppiumBy.ID,'plus').click()

        elif op=='*':
            self.driver.find_element(AppiumBy.ID,'mul').click()

        if num2 is not None:
            num2=self.driver.find_element(AppiumBy.ID,'digit'+str(num2))
            num2.click()

        equal=self.driver.find_element(AppiumBy.ID,'add_item')
        equal.click()

        code= 'new UiSelector().text("支出")'
        ele=self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,code)



    
        return ele.text

        sleep(10)
        input('input enter')

CA=calculator()
puls=CA.Simplecalculate('+',3,9)

result=CA.Simplecalculate('*',None,5)

print(result)