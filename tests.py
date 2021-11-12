import unittest
from task import conv_num

class TestCase(unittest.TestCase):
    # Tests for conv_num():
    # reject an empty string
    def test_empty_string(self):
        self.assertIsNone(conv_num(""))
    
    # reject not a string with a regular int
    def test_int(self):
        self.assertIsNone(conv_num(123))
    
    def test_string_int(self):
        self.assertEqual(conv_num("123"), "i'm an int")

    def test_negative_int(self):
        self.assertEqual(conv_num("-123"), "i'm an int")
    
    def test_float(self):
        self.assertEqual(conv_num("12.345"), "i'm a float")
    
    def test_negative_float(self):
        self.assertEqual(conv_num("-12.345"), "i'm a float")
    
    def test_multiple_decimal_points(self):
        self.assertIsNone(conv_num("12.1.23"))
    
    def test_hex(self):
        self.assertEqual(conv_num("0x1a2"), "i'm a hex")

    def test_negative_hex(self):
        self.assertEqual(conv_num("-0x1a2"), "i'm a hex")


if __name__ == '__main__':
    unittest.main()
