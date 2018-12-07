
# coding: utf-8

# In[2]:


import unittest
from salary import net_annual_salary

class TestNetSalary(unittest.TestCase):


    def test_net_annual(self):
        self.assertEqual(net_annual_salary(40,18),26208)
        self.assertEqual(net_annual_salary(35,75),81900)
        self.assertEqual(net_annual_salary(40,120),149760)
        self.assertEqual(net_annual_salary(60,32),59904)
        self.assertEqual(net_annual_salary(20,13),9464)

unittest.main()
