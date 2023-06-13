import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestNodeReverse(unittest.TestCase):

    def test_01_reverse_1(self):
        list_str = 'd'
        ll = Node.from_str(list_str)
        rl = ll.reverse()
        self.assertEqual('d', str(rl))

    def test_02_reverse_2(self):
        list_str = 'b, c'
        ll = Node.from_str(list_str)
        rl = ll.reverse()
        self.assertEqual('c, b', str(rl))

    def test_03_reverse_4(self):
        list_str = 'a, b, c, d'
        ll = Node.from_str(list_str)
        rl = ll.reverse()
        self.assertEqual('d, c, b, a', str(rl))

    def test_04_reverse_returns_new_list(self):
        original = Node.from_str('a, b, c, d')
        reversed_list = original.reverse()
        original.delete('b')
        self.assertEqual('a, c, d', str(original))
        self.assertEqual('d, c, b, a', str(reversed_list))
        reversed_list = reversed_list.delete('d')
        self.assertEqual('a, c, d', str(original))
        self.assertEqual('c, b, a', str(reversed_list))

