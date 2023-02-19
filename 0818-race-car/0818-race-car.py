class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        steps = 0
      
        while q:
            
            for _ in range(len(q)):
                cur_pos, cur_speed = q.popleft()
                
                if cur_pos == target:
                    return steps
                
                q.append((cur_pos + cur_speed, cur_speed*2))
                
                if (cur_speed > 0 and cur_pos +cur_speed > target) or (cur_pos + cur_speed < target and cur_speed < 0):
                    direc = -1 if cur_speed > 0 else 1
                    q.append((cur_pos, direc))
                
            
            steps += 1
        
        return steps
                    
                    
                
                
                    
                
                     
                
                
            