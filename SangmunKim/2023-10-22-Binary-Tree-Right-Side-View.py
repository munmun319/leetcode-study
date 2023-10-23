# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque([root])

        while q:
            right_side = None
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                result.append(right_side.val)
        
        return result

# Time complexity: O(n), visiting every node once
# Space complexity: O(n), maximum queue size is D/2