class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}
        hashset = set()
        ans = []
        for num in nums:
            cnt[num] = cnt.get(num,0)+1
            if cnt[num] > len(nums)//3 and num not in hashset:
                ans.append(num)
                hashset.add(num)
        return ans