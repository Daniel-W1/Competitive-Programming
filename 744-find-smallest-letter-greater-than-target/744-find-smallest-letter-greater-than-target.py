class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,h = 0,len(letters)-1
        while l <= h:
            mid = (l+h)//2
            if letters[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        for i in range(max(0,h),len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]
        