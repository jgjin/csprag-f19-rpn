import unittest

import rpn


class TestBasics(unittest.TestCase):
    def test_add(
            self,
    ):
        """Test added."""
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_sub(
            self,
    ):
        """Test subtracted."""
        result = rpn.calculate("3 2 -")
        self.assertEqual(1, result)

    def test_malformed_expr(
            self,
    ):
        """Test TypeError raised with malformed expression."""
        self.assertRaises(TypeError, rpn.calculate, "1 2 3")
