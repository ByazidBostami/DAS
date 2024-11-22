import numpy as np
class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem
        self.next = next


node = Node(5,None)
print(f"Element: {node.elem}, Next: {node.next }")


def create_list(arr):
    head = Node(arr[0],None)
    tail = head
    for i in range(len(arr)-1):
        n = Node(arr[i],None)
        tail.next = n 
        tail = tail.next
    return head 

