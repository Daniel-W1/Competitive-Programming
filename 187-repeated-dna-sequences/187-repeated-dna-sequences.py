class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        # so we are gonna do this like a pro,
        # we are gonna use hashing for O(n) sol
        # abcbbabc 3
        # 1*1 + 2*10 + 3*100
        window = collections.deque([])
        cnt = {}
        for i in range(10):
            window.append(s[i])
        cnt["".join(window)] = 1
        for i in range(10, len(s)):
            window.popleft()
            window.append(s[i])
            string = "".join(window)
            cnt[string] = cnt.get(string, 0) + 1
        return [k for k in cnt if cnt[k] > 1]