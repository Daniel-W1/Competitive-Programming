class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.precomp = []
        count = {}
        the_max = (0, 0)
        for num in self.persons:
            count[num] = count.get(num, 0) + 1
            if count[num] >= the_max[1]:
                the_max = (num, count[num])
            self.precomp.append(the_max[0])

    def q(self, t: int) -> int:
        index = self.binarySearch(self.times, t)
        return self.precomp[index]                

    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1 
            else:
                left = mid + 1
        return right

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)