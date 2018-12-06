import unittest 
from testmodules.TestModule1 import TestCalc 
from testmodules.TestModule2 import TestBmiCat
from testmodules.TestModule3 import TestNetSalary
from testmodules.TestModule4 import TestAgeCalc


def my_suite(): 
    suite = unittest.TestSuite() 
    result = unittest.TestResult() 
    suite.addTest(unittest.makeSuite(TestCalc)) 
    suite.addTest(unittest.makeSuite(TestBmiCat))
    suite.addTest(unittest.makeSuite(TestAgeCalc)) 
    suite.addTest(unittest.makeSuite(TestNetSalary))
    runner = unittest.TextTestRunner() 
    print(runner.run(suite)) 
my_suite()