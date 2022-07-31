class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            chars = "".join(sorted(list(word)))
            if chars not in groups:
                groups[chars] = [word]
            else:
                groups[chars].append(word)
        return groups.values()
            
                