class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# def insertNode(root,key):
#     if root is None:
#         return TreeNode(val=key)
#     else:
#         if root.val == key:
#             return root
#         elif root.val < key:
#             root.right = insertNode(root.right,key)
#         else:
#             root.left = insertNode(root.left,key)
#     return root

temp  =TreeNode(20,TreeNode(15,TreeNode(2)),TreeNode(7))
root = TreeNode(3,TreeNode(9),temp)



print(root)


def inOrderTraversal(root,count = 0):

    if root is None:
        return 0
 

    countLeft = inOrderTraversal(root.left,count + 1)
    countRight = inOrderTraversal(root.right, count + 1)
    print("leftCount",countLeft)
    print("rightCount",countRight)
    print(root.val)
    if countLeft > countRight:
        return countLeft +1
    else:
        return countRight + 1


answer  = inOrderTraversal(root,0)
print("answer",answer)






def maxDepth(root):
    print(root)