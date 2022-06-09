class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_map = {}
        for i,val in enumerate(nums):
            all_map[val] = i+1
        for i,val in enumerate(nums):
            if target-val in all_map and all_map[target-val] != i+1:
                return [i+1, all_map[target-val]]
        