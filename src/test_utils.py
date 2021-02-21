import utils
import unittest


class TestUtils(unittest.TestCase):
    def test_is_a_number(self):
        self.assertTrue(utils.is_a_number(3))
        self.assertTrue(utils.is_a_number(3.1415))
        self.assertTrue(utils.is_a_number(1 + 2j))
        self.assertFalse(utils.is_a_number("abc"))
        self.assertFalse(utils.is_a_number([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
