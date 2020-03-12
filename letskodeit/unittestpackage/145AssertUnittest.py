import unittest

class AssertDemo(unittest.TestCase):

#также смотри файл.там указаны все проверки
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not True")
        b = False
        self.assertFalse(b, 'b is not false')

    def test_assertEquals(self):
        a = 'Test'
        b = 'Test'
        self.assertEqual(a, b, msg='a is not equal to b')

    def test_assertNotEquals(self):
        a = 'Test'
        b = 'test'
        self.assertNotEqual(a, b, msg='a is not equal to b')

if __name__ == '__main__':
    unittest.main(verbosity=2)