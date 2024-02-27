# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []


        result = []

        level = 0
        queue.append([root,level])


        while len(queue)!=0:                
            element = queue.pop(0)
            # print("element",element,level)
            if element[0] is not None:
                if element[1] < len(result):
                    result[element[1]].append(element[0].val)
                else:
                    level = level + 1
                    result.append([element[0].val])
            
            if element[0] is not None and element[0].left is not None:
                queue.append([element[0].left,level])
            if element[0] is not None and element[0].right is not None:
                queue.append([element[0].right,level])
            # print(element)
        # print(result)

        return result
        
        