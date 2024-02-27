class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p = TreeNode(1,TreeNode(1),TreeNode(2))
q = TreeNode(1,TreeNode(1),TreeNode(2))

def traverse(p,q):
    if p is None and q is None:
        return True

    print(p.val,q.val)

    if p is not None and q is not None:
        return  (p.val == q.val) and traverse(p.left,q.left) and traverse(p.right,q.right)





def isSameTree(p, q):
    print(p,q)
    return traverse(p,q)

print(isSameTree(p,q))

