class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = set()
        def findall(i,ans):
            if i > len(nums)-1:
                output.add(tuple([nums[int(i)] for i in list(ans)]))
                return
            findall(i+1,ans+str(i))
            findall(i+1,ans)
        findall(0,"")
        return output
            