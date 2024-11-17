class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG


def getSize(root):
    if root is None:
        return 0
    left = getSize(root.left)
    right = getSize(root.right)
    return left+right+1

def get_size(root):
    if root is None:
        return 0
    size = 0
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        size += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return size

print(getSize(root))
print(get_size(root))