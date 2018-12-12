import unittest
from personal.fitness.classify import bmicat

class TestBmiCat(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        print('setupClass')
    def setUp(self):
        print('Set Up') 

    def test_bmicat(self):
        self.assertEqual(bmicat(16),'Underweight')
        self.assertEqual(bmicat(19),'Healthy')
        self.assertEqual(bmicat(22),'Healthy')
        self.assertEqual(bmicat(26),'Overweight')
        self.assertEqual(bmicat(31),'Obese')
        self.assertEqual(bmicat(40),'Morbidly Obese')
    
    def tearDown(self):
        print('Tear Down')     

@classmethod 
def tearDownClass(cls): 
    print('teardownClass')