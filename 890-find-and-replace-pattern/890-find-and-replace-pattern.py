class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def createPattern(pattern):
            pattern_map = {}
            new_pattern = ""
            cur = 1
            for char in pattern:
                if char in pattern_map:
                    new_pattern += pattern_map[char] + ","
                else:
                    new_pattern += str(cur) + ","
                    pattern_map[char] = str(cur)
                    cur += 1
            return new_pattern
        new_p = createPattern(pattern)
        output = []
        for word in words:
            p = createPattern(word)
            if p == new_p:
                output.append(word)
                
        
        return output
                
            