# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        graph=collections.defaultdict(list)
        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        visited=set()
        queue=collections.deque([start])
        time=-1
        while queue:
            time+=1
            for _ in range(len(queue)):
                current=queue.popleft()
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time 
        
        