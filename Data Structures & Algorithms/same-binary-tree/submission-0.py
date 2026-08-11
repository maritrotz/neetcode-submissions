from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        q1, q2 = deque([p]), deque([q])

        while q1:
            for i in range(len(q1)):
                pNode = q1.popleft()
                qNode = q2.popleft()

                if pNode is None and qNode is None:
                    continue
                if pNode is None or qNode is None or pNode.val != qNode.val:
                    return False
    

                q1.append(pNode.left) 
                q2.append(qNode.left)
                q1.append(pNode.right)
                q2.append(qNode.right)

        return True

        