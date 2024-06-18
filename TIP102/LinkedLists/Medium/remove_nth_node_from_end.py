# https://www.youtube.com/watch?v=gLybXQQgkiQ&list=PLrT2tZ9JRrf4cuavFcwQw6qfR8M9m7pEd&index=4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not(head):
            return
        
        #establish temp node
        temp = ListNode(0)
        #set temp node next to head of list
        temp.next = head

        #init slow and fast pointers to temp node
        slow_ptr = temp
        fast_ptr = temp

        #move fast pointer to n
        for i in range(n):
            fast_ptr = fast_ptr.next
        
        #while fast pointer is not at last node in list
        #move fast and slow pointers by 1
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        #when at end, node between fast and slow is target, 
        #set next node of slow pointer to the current fast pointer node
        slow_ptr.next = slow_ptr.next.next

        return temp.next
        

        