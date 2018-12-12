import unittest
from personal.identity.age import calculate_age



class TestAgeCalc(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        print('setupClass')
    def setUp(self):
        print('Set Up')
    
    def test_agecalc(self):
        self.assertEqual(calculate_age('2016-12-2'),'DOB must be a string of this format: YYYY-MM-DD')
        self.assertEqual(calculate_age('1987-12-30'),30 )
        self.assertEqual(calculate_age('2016-14-03'),'Month number cant be larger than 12')
        self.assertEqual(calculate_age('1963-02-08'),55)
        self.assertEqual(calculate_age('2016-05-34'),'Day number cant be larger than 31')
        self.assertEqual(calculate_age('2016-08-08'),2 )
    def tearDown(self):
        print('Tear Down')  
        
@classmethod 
def tearDownClass(cls): 
    print('teardownClass')   