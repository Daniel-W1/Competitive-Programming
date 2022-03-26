class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {2:"abc", 3:"def", 4:"ghi", 5: "jkl", 6: "mno", 7:"pqrs", 8: "tuv", 9: "wxyz"}
        if len(digits) < 2:
            if not digits: return []
            return list(hashmap[int(digits[0])])
        
        collect = list(hashmap[int(digits[-1])])
        auxillary = []
        
        for i in range(len(digits)-2, -1, -1):
            for j in hashmap[int(digits[i])]:
                for h in collect:
                    auxillary.append(j+h)
            collect = auxillary
            auxillary = []
        return collect
                    