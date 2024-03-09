class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        n1, n2 = len(nums1), len(nums2)
        
        while left < n1 and right < n2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        
        return -1