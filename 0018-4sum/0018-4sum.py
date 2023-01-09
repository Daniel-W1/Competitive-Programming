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
                
                # print(first_num, second_num)
                new_target = target - first_num - second_num
                left, right = idx2 + 1, n-1
                
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == new_target:
                        answer.append([first_num, second_num, nums[left], nums[right]])
                        the_left, the_right = nums[left], nums[right]
                        while left < right and nums[left] == the_left:
                            left += 1
                        while right > left and nums[right] == the_right:
                            right -= 1
                        
                    elif cur > new_target:
                        right -= 1
                    else:
                        left += 1
                    
                prev2 = second_num
                
            prev1 = first_num
            prev2 = inf
            
        return answer