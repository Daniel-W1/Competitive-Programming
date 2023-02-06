class Solution:
    def racecar(self, target: int) -> int:
        
        visited = set()
        q = deque([(0, 1)])
        steps = 0
        visited.add((0, 1))
        
        while q:
            
            for _ in range(len(q)):
                cur_pos, cur_speed = q.popleft()
                
                if cur_pos == target:
                    return steps
                
                if (cur_pos + cur_speed, cur_speed*2) not in visited:
                    q.append((cur_pos + cur_speed, cur_speed*2))
                    visited.add((cur_pos + cur_speed, cur_speed*2))
                
                if cur_speed > 0 and (cur_pos, -1) not in visited:
                    q.append((cur_pos, -1))
                    visited.add((cur_pos, -1))
                
                if cur_speed < 0 and (cur_pos, 1) not in visited:
                    q.append((cur_pos, 1))
                    visited.add((cur_pos, 1))
            
            steps += 1
        
        return steps
                    
                    
                
                
                    
                
                     
                
                
            