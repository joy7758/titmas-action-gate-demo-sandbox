import unittest

from demo_math import add, multiply


class DemoMathTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(4, 5), 20)


if __name__ == "__main__":
    unittest.main()
