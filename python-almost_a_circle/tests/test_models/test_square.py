#!/usr/bin/python3
"""
Defines unittests for square.py.
"""

import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """Unittests for testing Square class."""

    def test_id(self):
        s = Square(1, id=1)
        self.assertEqual(s.id, 1)


    def test_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_size_errors(self):
        with self.assertRaises(ValueError) as cm:
            s = Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        s = Square(2)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_str(self):
        s = Square(2, 3, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 3/1 - 2")

    def test_update(self):
        s = Square(1, 1, 1, 1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_args(self):
        s = Square(1, 1, 1, 1)
        s.update(89, 2)
        self.assertEqual(s.size, 2)

    def test_update_kwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(size=2)
        self.assertEqual(s.size, 2)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        s_dictionary = s.to_dictionary()
        expected = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dictionary, expected)
        self.assertIsInstance(s_dictionary, dict)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    def test_str_stdout(self):
        r = Square(2, 3, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (1) 3/1 - 2\n")

    def test_display_stdout(self):
        r = Square(2, 2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")


if __name__ == "__main__":
    unittest.main()
