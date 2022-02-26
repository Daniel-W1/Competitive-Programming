class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        ans = []
        if len(nums) == 1:
            return len(nums)
        for i in range(len(nums)):
            if i + 1 == len(nums): break
            in_dif = (nums[i+1] - nums[i])
            if in_dif: in_dif /= abs(in_dif)
            else: continue
            ans = nums[i:i+2]
            if max_len < len(nums) - i:
                index = i+2
                while index < len(nums):
                    check_dif = (nums[index] - nums[index-1])
                    if check_dif: check_dif /= abs(check_dif)
                    if check_dif == -1*in_dif:
                        ans.append(nums[index])
                    else:
                        index += 1
                        continue
                    index += 1
                    in_dif = check_dif
                max_len = max(max_len, len(ans))
                        
        return max_len if ans else 1
            
        