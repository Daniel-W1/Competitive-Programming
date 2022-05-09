class Solution:
    def goodDaysToRobBank(self, A: List[int], t: int) -> List[int]:
#         ans,pre = [], [0]*len(security)
#         cnt, prev = 0, 0
#         for i in range(1, len(security)):
#             if security[i] - prev <= 0:
#                 cnt += 1
#                 pre[i] = cnt
#             else:
#                 cnt = 0
#                 pre[i] = cnt
#             prev = security[i]
            
#         post, the_next,cnt = [0]*len(security), 0, 0
#         for i in range(len(security)-2, -1, -1):
#             if security[i] - the_next <= 0:
#                 cnt += 1
#                 post[i] = cnt
#             else:
#                 cnt = 0
#                 post[i] = cnt
#             the_next = security[i]
            
#         for i in range(len(security)):
#             if pre[i] >= time and post[i] >= time:
#                 ans.append(i)
#         print(pre, post)
#         return ans
        if t == 0: return list(range(len(A)))
        lft, rgt, n = [1], [1], len(A)
        
        # Build non-increasing on the left side (inclusive).
        curr = 1
        for i in range(1, n):
            if A[i] <= A[i - 1]: curr += 1
            else: curr = 1
            lft.append(curr)
        
        # Build non-decreasing on the right side (inclusive).
        curr = 1
        for i in range(n - 2, -1, -1):
            if A[i] <= A[i + 1]: curr += 1
            else: curr = 1
            rgt.append(curr)
        rgt.reverse()
        print(lft, rgt)
        return [i for i in range(n) if lft[i] >= t + 1 and rgt[i] >= t + 1]