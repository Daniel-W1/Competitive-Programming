class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        genes = ["A", "C", "G", "T"]
        bank = set(bank)
        
        queue = deque([start])
        answer = 0
        seen = set()
        
        while queue:
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == end:
                    return answer
                
                seen.add(cur)
                
                for idx in range(len(cur)):
                    # try to remove the current char
                    char = cur[idx]
                    for other in genes:
                        if other != char:
                            new = cur[:idx] + other + cur[idx + 1:]
                            if new in bank and new not in seen:
                                queue.append(new)
            answer += 1
        
        return -1
                            
                            
            
            
        