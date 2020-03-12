import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("i will run only once before all tests")
        print("#" * 30)

    def setUp(self):
        print("i will run once before every test")

    def test_method_A(self):
        print("running method A")

    def test_method_B(self):
        print("running method B")

    def tearDown(self):
        print("i will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("i will run only once after before all tests")
        print("#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)