# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))),TreeNode(2,None,TreeNode(3,None,TreeNode(4))))


def traverse(root):
    if root is None:
        return 0
    left = traverse(root.left)
    right = traverse(root.right)
    print(left,right)
    if left is False or right is False:
        return False
    if abs(left - right) > 1:
        # print(left,right,"issue found",root.left.val,root.right.val)
        return False

    return max(left,right) + 1
    

def isBalanced(root):
    # print(root)
    if traverse(root) == False:
        return False
    else:
        return True

print(isBalanced(root))
