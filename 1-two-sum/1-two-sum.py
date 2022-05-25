class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = i
        for i,val in enumerate(nums):
            if target - val in hashmap and hashmap[target-val] != i:
                return [i, hashmap[target-val]]
            