import unittest
from personal.identity.age import calculate_age

@classmethod 
def setUpClass(cls): 
    print('setupClass')

class TestAgeCalc(unittest.TestCase):
    def setUp(self):
        print('Set Up')
    
    def test_agecalc(self):
        self.assertEqual(calculate_age('1925-08-12'),93)
        self.assertEqual(calculate_age('1987-12-30'),30 )
        self.assertEqual(calculate_age('1954-03-25'),64)
        self.assertEqual(calculate_age('1963-02-08'),55)
        self.assertEqual(calculate_age('1923-05-25'),95)
        self.assertEqual(calculate_age('2016-08-08'),2 )
    def tearDown(self):
        print('Tear Down')  
        
@classmethod 
def tearDownClass(cls): 
    print('teardownClass')    