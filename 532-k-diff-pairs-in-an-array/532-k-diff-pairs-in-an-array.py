class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        charset = set()
        nums = sorted([(val,i) for i,val in enumerate(nums)])
        for val in nums:
            target = val[0]-k
            l,h = 0,len(nums)-1
            while l <= h:
                mid = (l+h)//2
                if nums[mid][0] == target:
                    if nums[mid][1] != val[1]:
                        charset.add((val[0],nums[mid][0]))
                        
                        charset.add((nums[mid][0],val[0]))
                    break
                elif nums[mid][0] > target:
                    h = mid-1
                else:
                    l = mid+1
        return len(charset)//2 if k else len(charset)