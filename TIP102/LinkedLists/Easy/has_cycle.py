

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, node):
        node.next = self
        return node


"""
Detecting cycle in linked list using fast and slow pointers
"""
def has_cycle_ptrs(listNode):
    if not listNode or listNode.next:
        return False
    
    fast = listNode.next
    slow = listNode

    while fast and fast.next:
        if fast == slow or fast.next == slow:
            return True
        
        fast = fast.next.next
        slow = slow.next

    return False


"""
Detecting cycle in linked list using a set
traverse the linked list and add each node to the set as long as all nodes are unique return false
"""
def has_cycle_set(listNode):
    list_set = set()
    while listNode:
        if listNode in list_set:
            return True

        list_set.add(listNode)
        listNode = listNode.next
    return False


my_list = Node(7).insert(Node(5))
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next}")
print(has_cycle_set(my_list))

my_list.next.next = my_list
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next.val}")
print(has_cycle_set(my_list))

"""
"List 5 --> 7 --> None"
False
"List 5 --> 7 --> 5"
True
"""

