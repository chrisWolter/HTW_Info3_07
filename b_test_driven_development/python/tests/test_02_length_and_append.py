import unittest

from b_test_driven_development.python.linkedlist.node import Node


class TestNodeLength(unittest.TestCase):
    """
    This class introduces a len() and append() function for the linked lists.
    Note that in order for len(linked_list) to work, you need to implement
    the __len__ method - see this site in the doc for more information:
    https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    """

    def test_01_len_1_element(self):
        linked_list = Node('a')
        expected = 1
        actual = len(linked_list)
        self.assertEqual(expected, actual)

    def test_02_len_2_elements(self):
        linked_list = Node('a', Node('b'))
        expected = 2
        actual = len(linked_list)
        self.assertEqual(expected, actual)

    def test_03_append_and_len_2(self):
        linked_list = Node('a')
        linked_list.append('b')
        expected = 2
        actual = len(linked_list)
        self.assertEqual(expected, actual)

    def test_04_append_and_len_3(self):
        ll = Node('a')
        ll.append('b')
        ll.append('c')
        actual = 3
        expected = len(ll)
        self.assertEqual(expected, actual)

    def test_05_append_and_last(self):
        ll = Node('a')
        ll.append('b')
        ll.append('c')
        ll.append('d')
        expected = 'd'
        actual = ll.last().data
        self.assertEqual(expected, actual)


