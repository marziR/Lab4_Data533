
# coding: utf-8

# In[2]:


import unittest
from TestAanu.TestModules.TestmeasureModule import TestCalc
from TestAanu.TestModules.TestclassifyModule import TestBmicat
from TestAanu.TestModules.TestageModule import TestAgeCalc
from TestAanu.TestModules.TestsalaryModule import TestNetSalary


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCalc))
    suite.addTest(unittest.makeSuite(TestBmicat))
    suite.addTest(unittest.makeSuite(TestAgeCalc))
    suite.addTest(unittest.makeSuite(TestNetSalary))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()

