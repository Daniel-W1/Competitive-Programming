class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        the_max_count = max(cnt.values())
        
        return sum(val for val in cnt.values() if val == the_max_count)