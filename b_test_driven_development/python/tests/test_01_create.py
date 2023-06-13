import unittest
from b_test_driven_development.python.linkedlist.node import Node


class TestNode(unittest.TestCase):

    def test_01_create_takes_data_as_parameter(self):
        linked_list = Node('a')
        expected = 'a'
        actual = linked_list.data
        self.assertEqual(expected, actual)

    def test_02_create_takes_next_node_as_optional_second_parameter(self):
        linked_list = Node('a', Node('b'))

    def test_03_last_returns_the_last_element_of_a_list(self):
        expected = last_node = Node('z')
        linkedlist = Node('v', Node('w', Node('x', Node('y', last_node))))
        actual = linkedlist.last()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
