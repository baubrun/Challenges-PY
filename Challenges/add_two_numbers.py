"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any
leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data



class LinkedList(object):
    def __init__(self, head=None):
        self.head = None

    def insert(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if not last_node.next:  # if at end of list
                    break
                last_node = last_node.next
            last_node.next = new_node # break next.none of node; set to new node

    def print_list(self):
        current_node = self.head
        while True:
            if not current_node:
                print("empty list")
                break
            else:
                print(current_node.data, end="-> ")
                current_node = current_node.next


    def __repr__(self):
        return self.head




ll = LinkedList()
first_node = Node("one")
ll.insert(first_node)

second_node = Node("two")
ll.insert(second_node)

# ll.print_list()
head = ll.head.next.next
print(head)