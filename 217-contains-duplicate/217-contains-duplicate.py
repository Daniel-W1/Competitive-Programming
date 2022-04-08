class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count = collections.Counter(nums)
        # for i in count:
        #     if count[i] > 1:
        #         return True
        # return False
    
        count = {}
        for i in nums:
            if count.get(i, False):
                return True
            count[i] = 1
        return False