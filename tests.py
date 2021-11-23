import unittest
from task import conv_num, my_datetime, conv_endian


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

    def test_conv_endian1(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_conv_endian2(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_conv_endian3(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_conv_endian4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_conv_endian5(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_conv_endian6(self):
        self.assertEqual(
            conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_conv_endian7(self):
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)

    def test_datetime0(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_datetime1(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_datetime2(self):
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_datetime3(self):
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def test_datetime4(self):
        self.assertEqual(my_datetime(45510215000), '02-29-3412')

    def test_datetime5(self):
        self.assertEqual(my_datetime(45510305000 ), '03-01-3412')

    def test_datetime6(self):
        self.assertEqual(my_datetime(45536601600), '12-31-3412')

    def test_datetime7(self):
        self.assertEqual(my_datetime(45536687999), '12-31-3412')

    def test_datetime8(self):
        self.assertEqual(my_datetime(45536688000), '12-31-3412')

    def test_datetime9(self):
        self.assertEqual(my_datetime(86400), '01-02-1970')


if __name__ == '__main__':
    unittest.main()
