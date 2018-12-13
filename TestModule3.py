import unittest
from personal.identity.salary import net_annual_salary


class TestNetSalary(unittest.TestCase):
    @classmethod 
    def setUpClass(cls): 
        print('setupClass')
    def setUp(self):
        print('Set Up')
    
    def test_net_annual(self):
        self.assertEqual(net_annual_salary(35,'b'),'both entries should be integer types')
        self.assertEqual(net_annual_salary(170,32),'a week has only 168 hrs!')
        self.assertEqual(net_annual_salary(20,15),10920)
        self.assertEqual(net_annual_salary(10,20),7280)
        self.assertEqual(net_annual_salary(50,10),18200)
        self.assertEqual(net_annual_salary(40,55),68640)
        
    def tearDown(self):
        print('Tear Down') 

    @classmethod 
    def tearDownClass(cls): 
        print('teardownClass')          