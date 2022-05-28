class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = {}
        for val in nums:
            if not cnt.get(val, False):
                cnt[val] = True
            else:
                return val