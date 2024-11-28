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

def preorder_using_stack(root):
    result = []
    stack = []
    stack.append(root)
    
    while len(stack) > 0:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
    
def preOrderTraversal(root):
    arr = []
    def traversal(node):
      if node is None:
        return
      arr.append(node.data)
      traversal(node.left)
      traversal(node.right)
    traversal(root)
    return arr

        
print(preOrderTraversal(root))
print(preorder_using_stack(root))