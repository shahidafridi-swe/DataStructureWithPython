# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None or p is None:
            if q is None and p is None:
                return True
            else:
                return False
        
        stack1 = []
        stack2 = []
    
        stack1.append(p)
        stack2.append(q)

        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            
            if node1.left or node2.left:
                if node1.left and node2.left:
                    stack1.append(node1.left)
                    stack2.append(node2.left)
                else:
                    return False
            if node1.right or node2.right: 
                if node1.right and node2.right:
                    stack1.append(node1.right)
                    stack2.append(node2.right)
                else:
                    return False
        return True 