import unittest
import random
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):
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

    def test_conv_num1(self):
        self.assertEqual(conv_num("99999"), 99999)

    def test_conv_num2(self):
        self.assertEqual(conv_num("0x677d"), 26493)


class TestConvEndian(unittest.TestCase):
    # Tests for conv_endian():
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

    def test_conv_endian8(self):
        self.assertEqual(conv_endian(0), '00')

    def test_conv_endian9(self):
        self.assertEqual(conv_endian(-0), '00')

    def test_conv_endian10(self):
        self.assertEqual(conv_endian(0, 'big'), '00')

    def test_conv_endian11(self):
        self.assertEqual(conv_endian(0, 'little'), '00')

    def test_conv_endian12(self):
        self.assertEqual(conv_endian(-0), '00')

    def test_conv_endian13(self):
        self.assertEqual(conv_endian(-1), '-01')

    def test_conv_endian14(self):
        self.assertEqual(conv_endian(15), '0F')

    def test_conv_endian15(self):
        self.assertEqual(conv_endian(16), '10')

    def test_conv_endian16(self):
        self.assertEqual(conv_endian(16, 'big'), '10')

    def test_conv_endian17(self):
        self.assertEqual(conv_endian(16, 'little'), '10')

    def test_conv_endian18(self):
        self.assertEqual(conv_endian(16, 'BIG'), None)

    def test_conv_endian19(self):
        self.assertEqual(conv_endian(1000000), '0F 42 40')

    def test_conv_endian20(self):
        self.assertEqual(conv_endian(4294967295), 'FF FF FF FF')

    def test_conv_endian21(self):
        self.assertEqual(conv_endian(4294967295, 'little'), 'FF FF FF FF')

    def test_conv_endian22(self):
        self.assertEqual(conv_endian(-4294967295), '-FF FF FF FF')

    def test_conv_endian23(self):
        self.assertEqual(conv_endian(4294967294), 'FF FF FF FE')

    def test_conv_endian24(self):
        self.assertEqual(conv_endian(4294967294, 'little'), 'FE FF FF FF')

    def test_conv_endian25(self):
        self.assertEqual(conv_endian(2659857920, 'little'), '00 36 8A 9E')

    def test_conv_endian26(self):
        self.assertEqual(conv_endian(111111, 'big'), '01 B2 07')

    def test_conv_endian27(self):
        self.assertEqual(conv_endian(000000, 'little'), '00')


def gen_convendian_testcases(tests_to_generate=1000):
    """Generates random tests for the conv_endian function. Adds tests
    to the TestConvEndian class."""
    for _ in range(tests_to_generate):
        num = random.randint(-4294967295, 4294967295)
        endian = random.choice(['big', 'little'])
        hex_raw = hex(abs(num))[2:].upper()
        hex_arr = []
        test_case = num, endian

        # Convert the raw hex string to the expected output
        if len(hex_raw) % 2 == 1:
            hex_arr.append('0' + hex_raw[0])
            start = 1
        else:
            start = 0

        for i in range(start, len(hex_raw), 2):
            hex_arr.append(hex_raw[i:i+2])

        if endian == 'little':
            hex_arr.reverse()

        expected = " ".join(hex_arr)

        if num < 0:
            expected = '-' + expected

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, test_case, conv_endian, message)
        setattr(TestConvEndian, 'test_{}'.format(test_case), new_test)


class TestMyDateTime(unittest.TestCase):
    # Tests for my_datetime():
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
        self.assertEqual(my_datetime(45510305000), '03-01-3412')

    def test_datetime6(self):
        self.assertEqual(my_datetime(45536601600), '12-31-3412')

    def test_datetime7(self):
        self.assertEqual(my_datetime(45536687999), '12-31-3412')

    def test_datetime8(self):
        self.assertEqual(my_datetime(45536688000), '12-31-3412')

    def test_datetime9(self):
        self.assertEqual(my_datetime(86400), '01-02-1970')


def build_test_func(expected, test_case, func_under_test, message):
    """Generic test builder function using assertEqual. test_case
    can be a single argument or multiple arguments as tuple."""
    def test(self):
        result = func_under_test(*test_case)
        self.assertEqual(expected,
                         result,
                         message.format(test_case, expected, result))
    return test


if __name__ == '__main__':
    gen_convendian_testcases(1000)
    unittest.main()
