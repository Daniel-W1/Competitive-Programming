class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, h = 0, len(people)-1
        boats = 0
        people.sort()
        while l <= h:
            curSum = people[l] + people[h]
            if curSum > limit:
                boats += 1
                h -= 1
            elif curSum <= limit:
                boats += 1
                l += 1
                h -= 1
            curSum = 0
            
        return boats
                
        return 4
        
                
            