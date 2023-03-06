import unittest
import calc


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
