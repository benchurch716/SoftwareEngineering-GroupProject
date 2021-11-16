import unittest
from task import conv_num


class TestCase(unittest.TestCase):
    # Tests for conv_num():
    # reject an empty string
    def test_empty_string(self):
        self.assertIsNone(conv_num(""))

    # reject non string
    def test_int(self):
        self.assertIsNone(conv_num(123))

    # test a positive int
    def test_string_int(self):
        self.assertEqual(conv_num("423"), 423)

    # test a negative int
    def test_negative_int(self):
        self.assertEqual(conv_num("-6478"), -6478)

    # test a positive float
    def test_float(self):
        self.assertEqual(conv_num("12.345"), 12.345)

    # test a negative float
    def test_negative_float(self):
        self.assertEqual(conv_num("-67.1245"), -67.1245)

    # reject more than 1 decimal points
    def test_multiple_decimal_points(self):
        self.assertIsNone(conv_num("12.1.23"))

    # test a positive hex
    def test_hex(self):
        self.assertEqual(conv_num("0xA"), int(0xA))

    # test a positive hex with lower case alpha
    def test_hex_lowercase(self):
        self.assertEqual(conv_num("0xb13c"), int(0xb13c))

    # test a negative hex value
    def test_negative_hex(self):
        self.assertEqual(conv_num("-0xF34b2"), int(-0xF34b2))

    # Test a hex number without he "0x"
    def test_hex_no_prefix(self):
        self.assertIsNone(conv_num("12345A"))

    # test a invalid hex value
    def test_invalid_hex(self):
        self.assertIsNone(conv_num("0xAZ4"))

    # test a decimal with only an integer component
    def test_int_float(self):
        self.assertEqual(conv_num('123.'), 123.0)


if __name__ == '__main__':
    unittest.main()
