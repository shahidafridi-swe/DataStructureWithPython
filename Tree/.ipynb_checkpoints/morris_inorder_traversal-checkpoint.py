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

def morris_inorder_traversal(root):
    current = root
    result = []

    while current:
        if current.left is None:
            result.append(current.data)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right 
            if predecessor.right is None:
                predecessor.right = current 
                current = current.left
            else:
                predecessor.right = None
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
print(morris_inorder_traversal(root))
 