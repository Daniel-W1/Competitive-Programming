class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        res, cnt = 0, Counter(nums)
        for num in nums:
            if target.startswith(num):
                nxt = target[len(num):]
                res += cnt[nxt]
                if nxt == num:
                    res -= 1
        
        return res
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined_list = nums1 + nums2
        combined_list.sort()
        print(combined_list)
        #if it's odd
        if len(combined_list) % 2 == 1:
            index = (len(combined_list) - 1) / 2
            median = combined_list[index]
        #if it's even
        else:
            index_high = len(combined_list) / 2
            index_low = index_high - 1
            print(combined_list[index_high])
            print(combined_list[index_low]) 
            median = (combined_list[index_high] + combined_list[index_low]) / 2.0
            print(median)
        return median
  def largestOverlap(self, A, B):
        N = len(A)
        LA = [i / N * 100 + i % N for i in xrange(N * N) if A[i / N][i % N]]
        LB = [i / N * 100 + i % N for i in xrange(N * N) if B[i / N][i % N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])
def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)
