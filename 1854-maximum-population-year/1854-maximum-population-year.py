class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        
        years = [0] * 101
        
        for birth, death in logs:
            birth -= 1950
            death -= 1950
            
            years[birth%100] += 1
            years[death%100] -= 1
        
        years = list(accumulate(years))
        # print(years)
        return 1950 + years.index(max(years))