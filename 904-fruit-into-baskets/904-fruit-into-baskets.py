class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, h = 0, 0
        max_fru = 0
        charSet = set()
        id_map = {}
        
        while h < len(fruits):
            while len(charSet) <= 2 and  h < len(fruits):
                id_map[fruits[h]] = h
                charSet.add(fruits[h])
                if len(charSet) > 2: break
                h += 1
            max_fru = max(max_fru, h-l)
            charSet.remove(fruits[min(id_map.values())])
            l = min(id_map.values()) + 1
            id_map.pop(fruits[min(id_map.values())])
            
        return max_fru