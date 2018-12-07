
# coding: utf-8

# In[1]:


import unittest
from measure import calc


class TestCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calc(81,1.80),25)
        self.assertEqual(calc(60,1.80),18)
        self.assertEqual(calc(76,1.50),33)
        self.assertEqual(calc(102,1.50),45)
        self.assertEqual(calc(65,1.70),22)

unittest.main()
