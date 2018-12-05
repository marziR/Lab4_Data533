
# coding: utf-8

# In[2]:


import unittest
from personal.fitness import classify

@classmethod
def setUpClass(cls):
    print('setupClass')

class TestBmicat(unittest.TestCase):
    def setUp(self):
        print('Set Up')

    def test_bmicat(self):
        self.assertEqual(bmicat(16), 'Underweight')
        self.assertEqual(bmicat(23), 'Healthy')
        self.assertEqual(bmicat(29), 'Overweight')
        self.assertEqual(bmicat(33), 'Obese')
        self.assertEqual(bmicat(52), 'Morbidly Obese')

    def tearDown(self):
        print('Tear Down')

@classmethod
def tearDownClass(cls):
    print('teardownClass')
