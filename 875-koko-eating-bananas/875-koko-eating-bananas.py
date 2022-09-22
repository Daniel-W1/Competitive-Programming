class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        okay here is what we are going to do
        
        so the most brutforce way is to iterate from 1 to -- 
        and return the first number that satisfies the condition
        
        but that would be O(sum(piles)*piles)
        and that is too costly
        
        so we can do it like this do BS and reduce the comp to O(logk*piles)
        

        question can i have no bananas ? 
        no u will have atleast 1 banana
        
        left = 0, right = sum(piles)
        so i want to finish all the bananas 
        so ya let's do it
        
        mid = (left + mid)//2
        iterate through my piles and see if i can make it out in h hours
        
        if i can i go down , if i can't i go up
        
        but how do i check whether i can make it out or not
        
        i can't do the easy math because the size of the piles are different
        
        how do we check part
        go through the whole thing and check  by how much hour i can finish that pile for example 30 with k = 16 takes 2 hours because ceil(30/16) is 2
        '''
        
        left, right = 0, sum(piles)
        ans = float('inf')
        
        while left <= right:
            mid = (left+right)//2
            hours = 0
            for pile in piles:
                if not mid: 
                    hours = float('inf')
                    break
                hours += ceil(pile/mid)
            
            if hours <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        