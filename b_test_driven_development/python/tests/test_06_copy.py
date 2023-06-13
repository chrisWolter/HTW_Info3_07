import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestNodeCopy(unittest.TestCase):

    def test_01_copy_1(self):
        ll = Node.from_str('g')
        copy = ll.copy()
        self.assertEqual('g', str(copy))

    def test_02_copy_modification_may_not_alter_original(self):
        original = Node.from_str('g')
        copy = original.copy()
        copy.data = 'h'
        self.assertEqual('h', str(copy))
        self.assertEqual('g', str(original))

    def test_02_copy_2(self):
        original = Node.from_str('b, c')
        copy = original.copy()
        self.assertEqual('b, c', str(copy))

    def test_03_copy_4(self):
        original = Node.from_str('a, b, c, d')
        copy = original.copy()
        self.assertEqual('a, b, c, d', str(copy))

    def test_04_ensure_copy(self):
        original = Node.from_str('a, b, c, d')
        copy = original.copy()
        original = original.delete('b')
        copy = copy.delete('c')
        self.assertEqual('a, c, d', str(original))
        self.assertEqual('a, b, d', str(copy))

        

