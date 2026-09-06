"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldtonew = {}
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            if curr not in oldtonew:
                oldtonew[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in oldtonew:
                    q.append(neighbor)
                    oldtonew[neighbor] = Node(neighbor.val)

                oldtonew[curr].neighbors.append(oldtonew[neighbor])

        return oldtonew[node]
        