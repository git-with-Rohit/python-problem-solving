import unittest
from solution import ListNode, add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):
    def list_to_nodes(self, lst):
        if not lst:
            return None
        node = ListNode(lst[0])
        current = node
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return node

    def nodes_to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test_add_two_numbers(self):
        l1 = self.list_to_nodes([2, 4, 3])
        l2 = self.list_to_nodes([5, 6, 4])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.nodes_to_list(result), [7, 0, 8])

    def test_add_two_numbers_with_carry(self):
        l1 = self.list_to_nodes([9, 9, 9])
        l2 = self.list_to_nodes([1])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.nodes_to_list(result), [0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()
