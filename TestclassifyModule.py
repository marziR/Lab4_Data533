
# coding: utf-8

# In[2]:


import unittest
from classify import bmicat


class TestBmicat(unittest.TestCase):

    def test_bmicat(self):
        self.assertEqual(bmicat(16), 'Underweight')
        self.assertEqual(bmicat(23), 'Healthy')
        self.assertEqual(bmicat(29), 'Overweight')
        self.assertEqual(bmicat(33), 'Obese')
        self.assertEqual(bmicat(52), 'Morbidly Obese')

unittest.main()
