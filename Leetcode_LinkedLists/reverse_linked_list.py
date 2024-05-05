# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        
        #if empty return
        if not(head):
            return
        
        #establish current and previous pointers
        current_node = head
        previous_node = None

        #while the current pointer is not None
        while current_node:
            #establish a temp pointer pointing to the next of current 
            temp_node = current_node.next

            #have the current pointer point to the previous pointer node
            current_node.next = previous_node

            #set the previous pointer node to the current pointer node
            previous_node = current_node

            #set the current pointer node to the temp pointer node 
            #which should be the one next to it and repeat 
            current_node = temp_node

        return previous_node

        