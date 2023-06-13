import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestNodeString(unittest.TestCase):
    """
    define a convenience factory method that
    constructs a linked list from a string.
    use this signature:

    @classmethod
    def from_str(cls, str_node):

    """

    def test_01_from_str(self):
        list_str = 'a, b, c, d'
        ll = Node.from_str(list_str)
        self.assertEqual(4, len(ll))
        self.assertEqual(list_str, str(ll))

    def test_02_from_str_l_1(self):
        list_str = 'd'
        ll = Node.from_str(list_str)
        self.assertEqual(1, len(ll))
