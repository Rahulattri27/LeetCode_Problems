class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def kthSmallest(root,k):
    n=0
    stack=[]
    cur=root
    while  cur or stack:
        while cur:
            stack.append(cur)
            print(stack)
            cur=cur.left
        cur=stack.pop()
        n+=1
        if n==k:
            return cur.val
        cur=cur.right
root=[3,1,4,None,2]
print(kthSmallest(root,2))
#only work on leetcode not in vscode