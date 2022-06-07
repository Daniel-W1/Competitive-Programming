class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        ans = [0]*len(nums1)
        while i < len(nums1)-len(nums2) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                ans[k] = nums2[j]
                j += 1
            else:
                ans[k] = nums1[i]
                i += 1
            k += 1
        while j < len(nums2):
            ans[k] = nums2[j]
            k += 1
            j += 1
        while i < len(nums1)-len(nums2):
            ans[k] = nums1[i]
            k += 1
            i += 1
        nums1[:] = ans
                
                
                
            
            
                    
            