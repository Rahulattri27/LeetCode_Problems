class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        def height_bool(root):
            if not root:
                return [True,0]
            left,right= height_bool(root.left),height_bool(root.right)

            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced,1+max(left[1],right[1])]
        return height_bool(root)[0]
