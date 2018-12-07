import unittest
from personal.fitness.measure import calc

@classmethod 
def setUpClass(cls): 
    print('setupClass')
    
class TestCalc(unittest.TestCase):
    def setUp(self):
        print('Set Up')

    def tearDown(self):
        print('Tear Down')

    def test_calc(self):
        self.assertEqual(calc(60,1.6),23)
        self.assertEqual(calc(85,1.8),26)
        self.assertEqual(calc(65,1.72),21)
        self.assertEqual(calc(85,1.53),36)
        self.assertEqual(calc(60,1.76),19)
        self.assertEqual(calc(85,1.88),24)
@classmethod 
def tearDownClass(cls): 
    print('teardownClass')   