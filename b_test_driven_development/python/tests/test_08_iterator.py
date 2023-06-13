import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestList(unittest.TestCase):
    """
    Implement an Iterator for the list -
    by implementing __iter__ all collection
    methods work for your list.

    see
    https://docs.python.org/3/glossary.html#term-iterator
    and
    https://docs.python.org/3/library/stdtypes.html#typeiter
    """

    def test_01_list_one(self):
        list_str = 'd'
        ll = Node.from_str(list_str)
        self.assertEqual(['d'], list(ll))

    def test_02_list_two(self):
        list_str = 'a, d'
        ll = Node.from_str(list_str)
        self.assertEqual(['a', 'd'], list(ll))

    def test_03_list_more(self):
        list_str = 'a, b, c, d, e'
        ll = Node.from_str(list_str)
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], list(ll))

    def test_04_set_more(self):
        list_str = 'a, b, c, d, e'
        ll = Node.from_str(list_str)
        self.assertEqual({'a', 'b', 'c', 'd', 'e'}, set(ll))

    def test_05_append_and_list(self):
        """
        the last tests called on a list created with
        multiple appends - this may show until now
        undetected issues in your implementation of append.
        """
        ll = Node('a')
        ll.append('b')
        ll.append('c')
        ll.append('d')
        expected = ['a', 'b', 'c', 'd']
        actual = list(ll)
        self.assertEqual(expected, actual)

    def test_06_loop(self):
        """
        if your iterator works correctly,
        you can use your list in a for each loop:
        """
        list_str = 'a, b, c, d, e'
        ll = Node.from_str(list_str)
        result = ""
        for e in ll:
            result += e
        self.assertEqual("abcde", result)

    def test_07_multiple_iterations(self):
        """
        your list should support multiple iterations
        """
        ll = Node.from_str('a, b, c, d, e')
        gen_list = list(ll)
        gen_set = set(ll)
        self.assertEqual(gen_set, set(gen_list))


