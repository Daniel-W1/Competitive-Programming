class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:       
        q = deque([("0000", 0)])
        visited = set(["0000"])
        deadends = set(deadends)
        
        if q[0][0] in deadends: return -1

        while q:            
            lock, moves = q.popleft()

            if lock == target:
                return moves

            for idx, char in enumerate(lock):
                new_lock1 = lock[:idx] + str((int(char) + 1)%10) + lock[idx+1:]
                new_lock2 = lock[:idx] + str((int(char) - 1)%10) + lock[idx+1:]
                
                if new_lock1 not in visited and new_lock1 not in deadends:
                    q.append((new_lock1, moves + 1))
                    visited.add(new_lock1)
                
                if new_lock2 not in visited and new_lock2 not in deadends:
                    q.append((new_lock2, moves + 1))
                    visited.add(new_lock2)

        return -1