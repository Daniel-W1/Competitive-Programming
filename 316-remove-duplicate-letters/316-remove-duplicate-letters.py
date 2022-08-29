class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        monoStack = []
        seen = [False for _ in range(26)]
        
        for letter in s:
            count[letter] -= 1
            if seen[ord(letter)-ord("a")]:
                continue
            while monoStack and monoStack[-1] > letter and count[monoStack[-1]] > 0:
                seen[ord(monoStack.pop())- ord("a")] = False

            monoStack.append(letter)
            seen[ord(letter)-ord("a")] = True
            
            
        return "".join(monoStack)