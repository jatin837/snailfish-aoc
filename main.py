class Node:
    def __init__(self, value=None, left=None, right=None, prev=None):
        self.value = value
        self.left = left
        self.right = right
        self.prev = prev


def serialize(node):
    if isinstance(node.value, int):
        return node.value
    return [serialize(node.left), serialize(node.right)]


def parse(fish):
    root = Node()
    if isinstance(fish, int):
        root.value = fish
        return root
    
    root.left = parse(fish[0])
    root.right = parse(fish[1])
    root.left.prev = root
    root.right.prev = root

    return root


def read_input(location='./input'):
    with open(location, 'r') as f:
        inp=(eval(i.strip()) for i in f.readlines())
    return next(inp), inp

def add(a, b):
    root = Node()
    root.left = a
    root.right = b
    return root

def reduce(root):
    pass

if __name__ == "__main__":
    first, inp = read_input()
    first = parse(first)
    for i in inp:
        first = add(first, parse(i))
        print(serialize(first))
        print(first)
        reduce(first)
