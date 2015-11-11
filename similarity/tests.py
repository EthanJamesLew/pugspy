import unittest
from sims import *

"""
Tests for PUGS similarity module using unittest
"""


class TestSimilarityMethods(unittest.TestCase):
    """
    Tests sims.py
    """
    def test_norm(self):
        self.vectors = [[0,3,4,5],[7,6,3,-1],[0,0,0]]
        self.assertEqual(norm(self.vectors[0]), 7.071)
        self.assertEqual(norm(self.vectors[2]), 0)
        self.assertEqual(norm(self.vectors[1]), 9.747)

    def test_unit(self):
        self.vectors = [[0,3,4,5],[7,6,3,-1],[0,0,0]]
        self.assertEqual(norm(unit(self.vectors[0])), 1.000)
        self.assertEqual(norm(unit(self.vectors[1])), 1.000)
        self.assertEqual(norm(unit(self.vectors[2])), None)

        self.assertEqual(unit(self.vectors[0]), [0.000, 0.424, 0.566, 0.707])
        self.assertEqual(unit(self.vectors[1]), [0.718,0.616,0.308,-.103])
        self.assertEqual(unit(self.vectors[2]), None)

    def test_nthroot(self):
        self.assertEqual(nth_root(3,4),1.316)
        self.assertEqual(nth_root(0,0),None)
        self.assertEqual(nth_root(3,-1),0.333)

    def test_cosine(self):
        self.vectors = [[3, 45, 7, 2], [2, 54, 13, 15],[0,0,0]]
        self.assertEqual(cosine(self.vectors[0], self.vectors[1]), 0.972)
        self.assertEqual(cosine(self.vectors[1], self.vectors[1]), 1.000)
        self.assertEqual(cosine(self.vectors[1], self.vectors[2]), None)

if __name__ == '__main__':
    unittest.main()
