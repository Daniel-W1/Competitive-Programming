class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         all_map = {}
#         for i,val in enumerate(nums):
#             all_map[val] = i+1
#         for i,val in enumerate(nums):
#             if target-val in all_map and all_map[target-val] != i+1:
#                 return [i+1, all_map[target-val]]
        def binarysearch(l,h,targ):
            while l <= h:
                mid = (l+h)//2
                if nums[mid] == targ:
                    return mid
                elif nums[mid] > targ:
                    h = mid -1
                else:
                    l = mid + 1
            return -1
        charset = set()
        for i,val in enumerate(nums):
            if val not in charset:
                new_target = target - val
                nums[i] = val-0.5
                if new_target >= val:
                    check = binarysearch(i, len(nums)-1,new_target)
                else:
                    check = binarysearch(0,i,new_target)
                if check >= 0:
                    return [i+1,check+1]
                nums[i] = val
                charset.add(val)


