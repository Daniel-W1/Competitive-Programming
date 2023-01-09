class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        # print(nums)
        prev1, prev2 = inf, inf
        answer = []
        
        for idx1 in range(n-3):
            first_num = nums[idx1]
            if first_num == prev1: continue
            
            for idx2 in range(idx1 + 1, n-2):
                second_num = nums[idx2]
                
                if second_num == prev2: continue
            
                new_target = target - first_num - second_num
                seen = set()
                prev3 = inf
                
                for idx in range(idx2 + 1, n):
                    if nums[idx] == prev3: continue
                        
                    if new_target - nums[idx] in seen:
                        val = new_target - nums[idx]
                        answer.append([first_num, second_num, val, nums[idx]])
                        prev3 = nums[idx]
                        
                    seen.add(nums[idx])
                    
                    
                prev2 = second_num
                
            prev1 = first_num
            prev2 = inf
            
        return answer