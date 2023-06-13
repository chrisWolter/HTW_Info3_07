import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestDelete(unittest.TestCase):
    """
    now we start with list manipulations.
    first: delete an element.
    note that the methods need to return
    a pointer to the first element of the
    list which needs to be updated in the
    tests!
    (otherwise it would not be possible to
    delete the first element)
    """

    def test_01_delete_one_element(self):
        ll = Node.from_str('d')
        ll = ll.delete('d')
        self.assertEqual(None, ll)

    def test_02_delete_two_first(self):
        ll = Node.from_str('x, y')
        ll = ll.delete('y')
        self.assertEqual('x', str(ll))

    def test_03_delete_two_last(self):
        ll = Node.from_str('x, y')
        ll = ll.delete('x')
        self.assertEqual('y', str(ll))

    def test_04_delete_longer_middle(self):
        list_str = 'a, b, c, d, e, f'
        ll = Node.from_str(list_str)
        ll = ll.delete('c')
        self.assertEqual('a, b, d, e, f', str(ll))

    def test_05_delete_first(self):
        list_str = 'a, b, c, d, e, f'
        ll = Node.from_str(list_str)
        ll = ll.delete('a')
        self.assertEqual('b, c, d, e, f', str(ll))

    def test_06_delete_last(self):
        list_str = 'a, b, c, d, e, f'
        ll = Node.from_str(list_str)
        ll = ll.delete('f')
        self.assertEqual('a, b, c, d, e', str(ll))

    def test_04_delete_multiple_occurences_all_should_be_deleted(self):
        list_str = 'a, b, c, d, e, c, f'
        ll = Node.from_str(list_str)
        ll = ll.delete('c')
        self.assertEqual('a, b, d, e, f', str(ll))

