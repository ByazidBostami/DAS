class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem 
        self.next = next

def create_list(arr):
    head = Node(arr[0],None)
    tail = head 

    for i in range(1,len(arr)):
        node = Node(arr[i],None) # new node
        tail.next = node #init address
        tail = tail.next #update new node address

    return head 

def count(head):
    count = 0
    temp = head
    while temp != None:
        count +=1
        temp = temp.next
    return count

arr = [1, 2, 3, 4, 5]
print(f"Created list = {create_list(arr)}")
a = create_list(arr)
print(f"Count = {count(a)}")
