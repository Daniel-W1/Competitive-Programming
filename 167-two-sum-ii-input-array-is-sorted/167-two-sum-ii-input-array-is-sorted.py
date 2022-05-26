class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        all_map = {}
        for i,val in enumerate(numbers):
            all_map[val] = i+1
        for i,val in enumerate(numbers):
            if target-val in all_map and all_map[target-val] !=  i+1:
                return [i+1,all_map[target-val]]