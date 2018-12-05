
# coding: utf-8

# In[3]:


import unittest
from personal.identity.age import calculate_age

@classmethod 
def setUpClass(cls): 
    print('setupClass')

class TestAgeCalc(unittest.TestCase):
    def setUp(self):
        print('Set Up')
    
    def test_agecalc(self):
        self.assertEqual(calculate_age('1937-11-11'),81)
        self.assertEqual(calculate_age('1964-04-17'),54)
        self.assertEqual(calculate_age('1976-01-25'),42)
        self.assertEqual(calculate_age('1989-08-04'),29)
        self.assertEqual(calculate_age('2001-07-07'),17)
        
    def tearDown(self):
        print('Tear Down')  
        
@classmethod 
def tearDownClass(cls): 
    print('teardownClass')  

