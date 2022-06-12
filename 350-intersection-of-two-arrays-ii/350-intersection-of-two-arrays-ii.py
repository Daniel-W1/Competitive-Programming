class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for num1 in cnt1:
            if cnt2.get(num1,False):
                for i in range(min(cnt1[num1],cnt2[num1])):
                    ans.append(num1)
        return ans