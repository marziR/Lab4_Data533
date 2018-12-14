
# coding: utf-8

# In[1]:


import unittest
from measure import calc


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('Set Up')

    def test_calc(self):
        self.assertEqual(calc(81,1.80),25.0)
        self.assertEqual(calc(37,1.45),17.6)
        self.assertEqual(calc(76,1.50),33.8)
        self.assertEqual(calc(102,1.50),45.3)
        self.assertEqual(calc(65,1.70),22.5)
        self.assertEqual(calc(81,6.0),'Value invalid!')
        self.assertEqual(calc(0,1.5),'Value invalid!')
        self.assertEqual(calc(56,0),'Cannot divide by 0')
        self.assertEqual(calc(56,-1),'Cannot divide by 0')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
unittest.main(argv=[''], verbosity=2, exit=False)
