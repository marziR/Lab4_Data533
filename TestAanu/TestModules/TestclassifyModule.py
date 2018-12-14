
# coding: utf-8

# In[2]:


import unittest
from classify import bmicat


class TestBmicat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('Set Up')

    def test_bmicat(self):
        self.assertEqual(bmicat(16), 'Underweight')
        self.assertEqual(bmicat(23), 'Healthy')
        self.assertEqual(bmicat(29), 'Overweight')
        self.assertEqual(bmicat(33), 'Obese')
        self.assertEqual(bmicat(52), 'Morbidly Obese')
        self.assertEqual(bmicat(0), 'Invalid BMI')
        self.assertEqual(bmicat('k'), 'Invalid Data Type')
        #self.assertEqual(bmicat('my bmi is 34'), 'Invalid Data Type')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
unittest.main(argv=[''], verbosity=2, exit=False)
