# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def compare_linked_list(l1, l2):
    if not (l1) and not (l2):
        return True
    if not (l1) or not (l2):
        return False
    if l1.val != l2.val:
        return False
    if l1.next == None:
        return l2.next == None
    return compare_linked_list(l1.next, l2.next)


def create_linked_list(values):
    l = ListNode(None)
    if values:
        for val in reversed(values):
            l.next = ListNode(val, l.next)
    return l.next

def print_linked_list(head: ListNode):
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next

def get_len_iter(head: ListNode):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def get_len_recursive(head: ListNode):
    if not head:
        return 0
    return get_len_recursive(head.next) + 1
