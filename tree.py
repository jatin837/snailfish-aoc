class Node:
    def __init__(self, value=None, left=None, right=None, prev=None):
        self.value = value
        self.left = left
        self.right = right
        self.prev = prev


def parse(fish):
    root = Node()
    if isinstance(fish, int):
        root.value = fish
        return fish
    
    root.left = parse(fish[0])
    root.right = parse(fish[1])
    root.left.prev = root
    root.right.prev = root

    return root

