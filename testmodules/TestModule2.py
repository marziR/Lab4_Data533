import unittest
from personal.fitness.classify import bmicat

@classmethod 
def setUpClass(cls): 
    print('setupClass')

class TestBmiCat(unittest.TestCase):
    def setUp(self):
        print('Set Up')

    

    def test_bmicat(self):
        self.assertEqual(bmicat(16),'UNDERWEIGHT')
        self.assertEqual(bmicat(19),'HEALTHY')
        self.assertEqual(bmicat(22),'HEALTHY')
        self.assertEqual(bmicat(36),'MORBIDLY OBESE')
        self.assertEqual(bmicat(31),'OBESE')
        self.assertEqual(bmicat(40),'MORBIDLY OBESE')
    
    def tearDown(self):
        print('Tear Down')     

@classmethod 
def tearDownClass(cls): 
    print('teardownClass')