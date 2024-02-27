class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def insertNode(root,key):
    if root is None:
        return TreeNode(val=key)
    else:
        if root.val == key:
            return root
        elif root.val<key:
            root.right = insertNode(root=root.right,key=key)
        else:
            root.left = insertNode(root=root.left,key=key)
    
    return root


root = insertNode(None,4)
insertNode(root,3)
insertNode(root,2)
insertNode(root,6)
insertNode(root,5)
insertNode(root,7)

def inOrderTraversal(root):
    if root == None:
        return 
    else:
        inOrderTraversal(root.left)
        print(root.val,root.left,root.right)
        inOrderTraversal(root.right)
inOrderTraversal(root=root)


def mirror(node):
    if node == None:
        return 
    
    mirror(node=node.left)
    mirror(node=node.right) 

    temp = node.right
    node.right =node.left
    node.left = temp


mirror(root)
print("------------")
inOrderTraversal(root=root)







print(root)











def invertTree(root):
    print(root)




# print(invertTree())