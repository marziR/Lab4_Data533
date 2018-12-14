
import unittest
from personal.fitness.measure import calc

    
class TestCalc(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        print('setupClass')
    def setUp(self):
        print('Set Up')
    def tearDown(self):
        print('Tear Down')

    def test_calc(self):
        self.assertEqual(calc(160,0),'Division by 0,height cant be zero!')
        self.assertEqual(calc(85,'b'),'both entries must be numbers')
        self.assertEqual(calc(65,1.72),21)
        self.assertEqual(calc(85,1.53),36)
        self.assertEqual(calc(60,1.76),19)
        self.assertEqual(calc(85,1.88),24)
    @classmethod 
    def tearDownClass(cls):
        print('teardownClass')  
