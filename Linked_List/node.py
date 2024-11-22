class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem
        self.next = next


node = Node(5,None)
print(f"Element: {node.elem}, Next: {node.next }")