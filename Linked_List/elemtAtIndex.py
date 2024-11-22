class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem
        self.next = next 


def create_list(arr):
    head = Node(arr[0],None)
    tail = head
    for i in range(1, len(arr)):
        node = Node(arr[i],None)
        tail.next = node
        tail = tail.next 
    return head

def elem_at(head,index):
    count = 0 
    temp = head
    while temp != None:
        if count == index:
            return temp.elem
        temp = temp.next
        count +=1

    return None

arr = [1, 2, 3, 4, 5]
link_list = create_list(arr)
print(elem_at(link_list,3))