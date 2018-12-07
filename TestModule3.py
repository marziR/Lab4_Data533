import unittest
from personal.identity.salary import net_annual_salary

@classmethod 
def setUpClass(cls): 
    print('setupClass')

class TestNetSalary(unittest.TestCase):
    def setUp(self):
        print('Set Up')
    
    def test_net_annual(self):
        self.assertEqual(net_annual_salary(30,20),21840)
        self.assertEqual(net_annual_salary(40,32),39936)
        self.assertEqual(net_annual_salary(20,15),10920)
        self.assertEqual(net_annual_salary(10,20),7280)
        self.assertEqual(net_annual_salary(50,10),18200)
        self.assertEqual(net_annual_salary(40,55),68640)
        
    def tearDown(self):
        print('Tear Down') 

@classmethod 
def tearDownClass(cls): 
    print('teardownClass')          