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


def inorder_using_stack(root):
    result = []
    stack = []
    current = root
    
    while current or len(stack) > 0:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    return result
    
def inOrderTraversal(root):
    arr = []
    def traversal(node):
      if node is None:
        return
      traversal(node.left)
      arr.append(node.data)
      traversal(node.right)
    traversal(root)
    return arr
        
print(inOrderTraversal(root))
print(inorder_using_stack(root))