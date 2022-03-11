class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # new = []
        # for val in nums:
        #     if val < 0:
        #         new.append(-1*val)
        #     else:
        #         new.append(val)
        # return [val**2 for val in sorted(new)]
        h = 0
        while h < len(nums) and nums[h] < 0:
            h += 1
        if h == 0 or h == len(nums): 
            if h == 0:
                return [val**2 for val in nums]
            return [val**2 for val in nums][::-1]
        
        l = h-1
        ans = []
        while h < len(nums) and l >= 0:
            if l >=0 and nums[h]**2 < nums[l]**2:
                ans.append(nums[h]**2)
                h += 1
            elif l >= 0 and nums[h]**2 > nums[l]**2:
                ans.append(nums[l]**2)
                l -= 1
            elif l >= 0:
                ans.append(nums[l]**2)
                l -= 1
    
        if l >= 0:
            return ans + [val**2 for val in nums[:l+1]][::-1]
        elif h < len(nums):
            return ans + [val**2 for val in nums[h:]]
        return ans