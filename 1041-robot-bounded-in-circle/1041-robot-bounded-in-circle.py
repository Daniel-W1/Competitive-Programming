class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        idx = 0
        pos = [0, 0]
        
        for _ in range(4):
            for inst in instructions:
                
                if inst == "L":
                    idx += 1
                    idx %= 4
                
                elif inst == "R":
                    idx += 3
                    idx %= 4
                
                else:
                    cur_dir = dirs[idx]
                    pos = [pos[0] + cur_dir[0], pos[1] + cur_dir[1]]
        
        return pos == [0, 0]
                    
                    