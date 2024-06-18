# https://realpython.com/linked-lists-python/

"""
The only information you need to store for a linked list is 
where the list starts (the head of the list). Next, create 
another class to represent each node of the linked list:
"""    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
    def __repr__(self):
        return self.data


"""
Here’s a slight change to the linked list’s __init__() 
that allows you to quickly create linked lists with some data:
"""
class LinkedList:
    "INIT LINKED LIST WITH DATA ITERABLE"
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    """
    You can also add a __repr__ to both classes to have a 
    more helpful representation of the objects:
    """
    def __repr__(self):
        node = self.head
        
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    "TRAVERSE LINKED LIST"
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    """
    Remove node in Linked List
    To remove a node from a linked list, 
    you first need to traverse the list until you 
    find the node you want to remove. Once you find 
    the target, you want to link its previous and next nodes. 
    This re-linking is what removes the target node from the list.
    """
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is Empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise Exception(f'Node with data "{target_node_data}" is not found')

"""
In the above class definition, you can see the two main 
elements of every single node: data and next. 
You can also add a __repr__ to both classes to have 
a more helpful representation of the objects:
""" 

"CREATE LINKED LIST"
# llist_1 = LinkedList()
# print(llist_1)
# # None

# first_node = Node("1")
# llist_1.head = first_node
# # 1 -> None

# second_node = Node("2")
# first_node.next = second_node
# third_node = Node("3")
# second_node.next = third_node
# print(llist_1)
# # 1->2->3->None

"TRAVERSE LINKED LIST"
# llist_2 = LinkedList(["a", "b", "c", "d", "e"])
# print(llist_2)
# # a -> b -> c -> d -> e -> None

# for node in llist_2:
#     print(node)

"REMOVE NODE"
# llist = LinkedList()
# llist.remove_node("a")
# Exception: List is empty

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

llist.remove_node("c")
print(llist)
# a -> b -> c -> d -> e -> None
# a -> b -> d -> e -> None

llist.remove_node("f")
# Exception: Node with data 'f' not found

"IMPLEMEMT DOUBLE AND CIRCLE LL"









