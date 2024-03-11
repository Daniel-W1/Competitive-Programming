class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        
        answer = []
        for char in order:
            for count in range(cnt[char]):
                answer.append(char)
        
        for char in s:
            if char not in order:
                answer.append(char)
        
        return "".join(answer)
            