import unittest
from letskodeit.unittestpackage.test_case_demo import TestCaseDemo
from letskodeit.unittestpackage.test_case_demo_two import TestCaseDemoTwo

#get all test from 1st testcasedemo and 2st testcasedemo
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemoTwo)

#create a test suite
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

