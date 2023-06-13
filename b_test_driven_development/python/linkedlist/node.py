class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __len__(self):
        count = 1
        current = self
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        new_node = Node(data)
        current = self
        while current.next is not None:
            current = current.next
        current.next = new_node

    def last(self):
        current = self
        while current.next is not None:
            current = current.next
        return current

    def __str__(self):
        elements = []
        current = self
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return ', '.join(elements)

    def __iter__(self):
        current = self
        while current is not None:
            yield current.data
            current = current.next

    @classmethod
    def from_str(cls, str_node):
        data_list = str_node.split(', ')
        head = None
        current = None
        for data in data_list:
            new_node = cls(data.strip())
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
        return head

    def delete(self, data):
        # Handle the case where the first node needs to be deleted
        while self.data == data:
            self = self.next
            if self is None:
                return None

        current = self
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next

        return self

    def copy(self):
        copied_head = Node(self.data)
        current = self.next
        copied_current = copied_head

        while current is not None:
            copied_node = Node(current.data)
            copied_current.next = copied_node
            copied_current = copied_current.next
            current = current.next

        return copied_head

    def reverse(self):
        reversed_list = None
        current_node = self

        while current_node:
            new_node = Node(current_node.data)
            new_node.next = reversed_list
            reversed_list = new_node
            current_node = current_node.next

        return reversed_list