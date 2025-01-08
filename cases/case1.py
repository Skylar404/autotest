from hytest import *
from AppiumTest.calculator import *

class TestCase01:
    name = '计算器测试'
    def teststeps(self):
        STEP(1, '3+9=12')
        puls=CA.Simplecalculate('+',3,9)
        print(puls)
        CA.btn_cancel()
        STEP(2, '12*5=60')
        result=CA.Simplecalculate('*',None,5)
        print(result)
        STEP(3, '验证结果')
        CHECK_POINT('验证结果',int(result)==60)