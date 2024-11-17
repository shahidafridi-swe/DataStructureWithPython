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

def postorder_using_stack(root):
    result = []
    stack1 = []
    stack2 = []
    
    stack1.append(root)
    
    while len(stack1) > 0:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        result.append(stack2.pop().data)
    return result
    
def postOrderTraversal(root):
    arr = []
    def traversal(node):
      if node is None:
        return
      traversal(node.left)
      traversal(node.right)
      arr.append(node.data)
    traversal(root)
    return arr

        
print(postOrderTraversal(root))
print(postorder_using_stack(root))