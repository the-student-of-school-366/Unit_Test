
import unittest
from rectangle import area


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)


    def test_rectangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_types(self):
        self.assertRaises(TypeError, area, 'Five')


