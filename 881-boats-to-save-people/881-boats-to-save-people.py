class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [3,2,2,1]
        # [1,2,2,3]
        #        ||
        # curTotal 3
        # curTotal 
        # [1,2,4,5]
        people.sort()
        boats = 0
        left, right = 0, len(people)-1
        
        while left <= right:
            cur = people[left] + people[right]
            if cur <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        return boats
                
            