from unittest import TestCase

from linear_search import linear_search

class Test(TestCase):
    def test_linear_search(self):
        res = linear_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(True, res)
