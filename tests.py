import unittest
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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


if __name__ == '__main__':
    unittest.main()
