import unittest

class Calc:
    def sum(self, a, b):
        return a+b

    def divide(self, a, b):
        return round(float(a)/float(b), 2)

    def sub(self, a, b):
        return a-b

    def multi(self, a, b):
        return round(a*b, 2)


class TestStringMethods(unittest.TestCase):
    def test_sum(self):
        c = Calc()
        self.assertEqual(c.sum(7,8), 15)

    def test_sub(self):
        c = Calc()
        self.assertEqual(c.sub(7,8), -1)

    def test_divide(self):
        c = Calc()
        self.assertEqual(c.divide(7,8), 0.88)

    def test_multi(self):
        c = Calc()
        self.assertEqual(c.multi(-8.127,-2), 16.25)

if __name__ == '__main__':
    unittest.main()
