import LinkedList
import test_solution

# l1 = LinkedList.create_linked_list([1, 2, 3, 4, 5])
# l2 = LinkedList.create_linked_list([1, 2, 4, 4, 5])


def delete_duplicates_codepath(head: LinkedList) -> LinkedList:
    # init the slow and fast pointers at head of list
    slow = head
    fast = head

    # traverse the list
    while slow and fast:

        # move fast pointer until a non duplicate node or until fast == None
        while fast and fast.val == slow.val:
            fast = fast.next

        # cut out the duplicate node and move slow to current node of fast
        slow.next = fast
        slow = fast

    # return head
    return head


def delete_duplicates_oneptr(head: LinkedList) -> LinkedList:
    #init ptr at start
    current_node = head
    
    #traverse list
    while current_node:
        
        #while not at last node and duplicate nodes found, iterate ptr until non duplicate node
        while current_node.next and current_node.next.val == current_node.val:
            current_node.next = current_node.next.next
        
        #move ptr to non duplicate node
        current_node = current_node.next
    
    return head

def delete_duplicates_twoptr(head: LinkedList) -> LinkedList:
    if not(head):
        return 
    
    #init current and previous nodes, one at start and one at start+1
    previous = head
    current = head.next
    
    #traverse list
    while current:
        
        #if duplicate values then:
            #cut the duplicate node and move the current pointer
        if current.val == previous.val:
            previous.next = current.next
            current = previous.next
        
        #if not duplicate then move ptrs
        else:
            previous = current
            current = current.next
    
    return head

print("Testing delete_duplicates_codepath")
test_solution.test_solution(delete_duplicates_codepath)

print("")

print("Testing delete_duplicates_oneptr")
test_solution.test_solution(delete_duplicates_oneptr)

print("")

print("Testing delete_duplicates_oneptr")
test_solution.test_solution(delete_duplicates_twoptr)
