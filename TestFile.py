import unittest 
from TestModule1 import TestCalc 
from TestModule2 import TestBmiCat
from TestModule3 import TestNetSalary
from TestModule4 import TestAgeCalc


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