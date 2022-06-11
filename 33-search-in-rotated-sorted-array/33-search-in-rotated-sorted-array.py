class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0,len(nums)-1
        # this part is just trying to find the maximum in the array
        
        while l < h:
            mid = (l+h)//2
            if nums[l] < nums[mid]:
                l = mid
            else:
                h = mid
        h = len(nums)-1
        def binarysearch(l,h):
            while l <= h:
                mid = (l+h)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    h = mid-1
                else:
                    l = mid+1
            return -1
        res1 = binarysearch(0,l)
        res2 = binarysearch(l+1,h)
        
        return max(res1,res2)
    
        