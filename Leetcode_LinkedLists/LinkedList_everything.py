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


def deleteDuplicates(head):
    # one pointer approach-----------------------
    current_node = head
    print("printing original:")
    print_linked_list(head)

    while current_node:
        while current_node.next and current_node.next.val == current_node.val:
            current_node.next = current_node.next.next

        current_node = current_node.next
    
    print("printing mod list:")
    print_linked_list(head)
    return head

    # two pointer approach---------------------
    if not (head):
        return

    previous_node = head
    current_node = head.next

    while current_node:
        if current_node.val == previous_node.val:
            previous_node.next = current_node.next
            current_node = previous_node.next

        else:
            previous_node = current_node
            current_node = current_node.next

    return head

    # codepath solution------------------
    slow_ptr = head
    fast_ptr = head

    while slow_ptr and fast_ptr:
        while fast_ptr and slow_ptr.val == fast_ptr.val:
            fast_ptr = fast_ptr.next

        slow_ptr.next = fast_ptr
        slow_ptr = fast_ptr

    return head

newList_head=create_linked_list([1,1,2,3,3])
# print("printing original list")
# print_linked_list(newList_head)

mod_list = deleteDuplicates(newList_head)

# print("printing mod list")
# print_linked_list(mod_list)