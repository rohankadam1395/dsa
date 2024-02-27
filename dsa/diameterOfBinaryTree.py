# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [1,2,3,4,5]
        
root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))

def dfsGetLastNode(root):
    if root is None:
        return 0
    
    print(root.val)
    left =dfsGetLastNode(root.left)
    right= dfsGetLastNode(root.right)
    print("___",left,right)

    return max(left,right) + 1



def diameterOfBinaryTree(root):
    print(root)
    ans = dfsGetLastNode(root)
    print("answer: ",ans)




print(diameterOfBinaryTree(root))