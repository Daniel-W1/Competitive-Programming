class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        first_map = {}
        for i,val in enumerate(list(secret)):
            if val in first_map:
                first_map[val][1] += 1
            else:
                first_map[val] = [set(),1]
            first_map[val][0].add(i)
        cow_count = 0
        bull_count = 0
        for i,val in enumerate(list(guess)):
            if val in first_map:
                if i in first_map[val][0]:
                    cow_count += 1
                    first_map[val][1] -= 1
        for i,val in enumerate(list(guess)):  
            if val in first_map:
                if first_map[val][1] > 0 and i not in first_map[val][0]:
                    bull_count += 1
                    first_map[val][1] -= 1
        return str(cow_count)+"A"+str(bull_count)+"B"
        
            
            