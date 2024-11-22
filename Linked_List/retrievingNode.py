class Node:
    def __init__(self, elem = None , next = None):
        self.elem = elem
        self.next = next 


def create_list(linklist):
    head = Node(linklist[0],None)
    tail = head

    for i in range(1,len(linklist)):
        node = Node(linklist[i],None)
        tail.next = node
        tail = tail.next

    return head



def nodeAtt(head, index):
    count = 0 
    temp = head
    while temp != None:
        if count == index:
            return temp 
        temp = temp.next
        count += 1

    return None
arr = ([1,2,3,4,5,6,7,9])
link_list = create_list(arr)
node = nodeAtt(link_list, 4)
print(node)