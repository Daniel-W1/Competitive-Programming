class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        all_cnt = {i:Counter(words[i]) for i in range(len(words))}
        prev = all_cnt[0]
        for i in range(1,len(words)):
            final = {}
            for char in prev:
                if char in all_cnt[i]:
                    final[char] = min(prev[char],all_cnt[i][char])
            prev = final
        ans = []
        for char in final:
            for cnt in range(final[char]):
                ans.append(char)
        return ans
            