class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twosum(l,r,target):
            if l > r: return -1
            while l < r:
                cur_sum = nums[l]+nums[r]
                if cur_sum == target:
                    output.append([-target, nums[l], nums[r]])
                    cur_right = nums[r]
                    while r > l and nums[r] == cur_right:
                        r -= 1
                    
                elif cur_sum > target:
                    r -= 1
                else:
                    l += 1
        output = []
        prev = None
        for i,num in enumerate(nums):
            if prev != None and num == prev:
                continue
            prev = num
            new_target = - num
            twosum(i+1, len(nums)-1, new_target)
    
        return output
            
            
                