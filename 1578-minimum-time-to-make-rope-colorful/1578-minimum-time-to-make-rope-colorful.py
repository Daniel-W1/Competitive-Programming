class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        aaa
        | |
        
        
        Input: colors = "aabaa", neededTime = [1,2,3,4,1]
                            ||
        '''
        left = 0
        cost = 0
        
        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                cost += min(neededTime[left], neededTime[right])
                
                if neededTime[left] < neededTime[right]:
                    left = right
    
            else:
                left = right
        
        return cost
            