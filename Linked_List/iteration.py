import numpy as np
class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem 
        self.next = next 

def create_list(arr):
    head = Node(arr[0],None) #First element with None address
    tail = head 
    for i in range(1, len(arr)):
        node = Node(arr[i],None) #create new node
        tail.next = node #link tail to new node
        tail = tail.next #update tail address

    return head



def iteration(head):
    temp = head 
    while temp != None:
        print(temp.elem)
        temp = temp.next




arr = [1, 2, 3, 4, 5]
linked_list_head = create_list(arr)

print("Linked list elements:")
iteration(linked_list_head)