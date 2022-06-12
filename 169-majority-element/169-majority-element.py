class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        the_count = Counter(nums)
        for val in the_count:
            if the_count[val] > len(nums)/2:
                return val