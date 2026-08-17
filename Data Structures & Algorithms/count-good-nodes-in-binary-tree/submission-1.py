# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        res = []
        if root:
            q.append((root, root.val))
        else:
            return 0

        while q:
            for i in range(len(q)):
                node, max_val = q.popleft()
                if node.val >= max_val:
                    res.append(node.val)
                
                current_max = max(max_val, node.val)
                if node.left:
                    q.append((node.left, current_max))
                if node.right:
                    q.append((node.right, current_max))

        return len(res)



        