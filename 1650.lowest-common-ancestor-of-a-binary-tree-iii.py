"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent_p = set([p])
        parent_q = set([q])

        node = p.parent
        while node is not None:
            parent_p.add(node)
            node = node.parent
        
        node = q
        while node is not None:
            if node in parent_p:
                return node
            node = node.parent
        
        return None