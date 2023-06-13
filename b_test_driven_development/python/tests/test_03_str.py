import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestNodeString(unittest.TestCase):
    """
    create a concise string representation of your
    linked list which especially eases further testing.
    use:
    def __str__(self): ...
    """

    def test_01_to_str(self):
        """
        this is the last test using the explicit form with
        actual and expected variables, as with these very
        short test not using them is actually more readable.
        """
        ll = Node('a')
        expected = 'a'
        actual = str(ll)
        self.assertEqual(expected, actual)

    def test_02_append(self):

        ll = Node('a')
        ll.append('b')
        self.assertEqual('a, b', str(ll))

    def test_03_append_3(self):
        ll = Node('a')
        ll.append('b')
        ll.append('c')
        self.assertEqual('a, b, c', str(ll))

    def test_03_append_4(self):
        ll = Node('a')
        ll.append('b')
        ll.append('c')
        ll.append('d')
        self.assertEqual('a, b, c, d', str(ll))
