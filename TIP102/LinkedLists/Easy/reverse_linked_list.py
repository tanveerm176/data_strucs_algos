import LinkedList
import test_solution

def reverse_linked_list(head:LinkedList)->LinkedList:
    if not(head):
        return
    
    #init pointers at head and at None
    #since None will be the last element of the reversed list
    current_ptr = head
    previous_ptr = None
    
    #traverse list using current ptr
    while current_ptr:
        
        #create a temp ptr and point to node next to current
        temp_ptr = current_ptr.next
        
        #set the next ptr of currrent to previous node
        current_ptr.next = previous_ptr
        
        #move current and previous ptrs 
        previous_ptr = current_ptr
        current_ptr = temp_ptr
    
    #return previous ptr since that is the new head
    return previous_ptr

test_solution.test_solution(reverse_linked_list)

        