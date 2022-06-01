# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q = collections.deque()
        q.append((root,0))
        ans = [[q[0][0].val]]
        other_q = []
        while q:
            level = q[0][1]
            out = []
            while q and q[0][1] == level:
                if q[0][0].right or q[0][0].left:
                    if q[0][0].left:
                        out.append(q[0][0].left.val)
                        q.append((q[0][0].left,level+1))
                        other_q.append((q[0][0].left.val,level+1))
                    if q[0][0].right:
                        out.append(q[0][0].right.val)
                        q.append((q[0][0].right,level+1))
                        other_q.append((q[0][0].right.val,level+1))
                q.popleft()
            ans.append(out)
        ans.pop()
        return ans
                        
        