class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        
        answer = []
        for char in order:
            for count in range(cnt[char]):
                answer.append(char)
        
        for char in cnt:
            if char not in order:
                for count in range(cnt[char]):
                    answer.append(char)
        
        return "".join(answer)
            