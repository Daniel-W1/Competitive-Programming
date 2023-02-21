class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        
        starting = (0, 0)
        
        n, m = len(grid), len(grid[0])
        cnt = 0
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        for r in range(n):
            for c in range(m):
                
                if grid[r][c] == "@":
                    starting = (r, c)
                
                elif grid[r][c] not in ".#" and grid[r][c].islower():
                    cnt += 1
            grid[r] = list(grid[r])
            # print(grid[r])
            
        # print(grid)
        
        directions = [(1, 0), (0, 1),(-1, 0),(0,-1)]
        visited = set()
        q = deque([(starting[0], starting[1], "")])
        visited.add((starting[0], starting[1], ""))
        
        ans = inf
        steps = 0
        while q:
            
            for _ in range(len(q)):
                r, c, keys = q.popleft()

                # print(r, c, keys, steps)
                if len(keys) == cnt:
                    return steps


                for dx, dy in directions:
                    newr, newc  = r + dx, c + dy
                    
                    if inbound(newr, newc) and grid[newr][newc] != "#":
                        
                        
                        if grid[newr][newc] in ".@" and (newr, newc, keys) not in visited:
                            visited.add((newr, newc, keys))
                            q.append((newr, newc, str(keys)))

                        elif grid[newr][newc] in "abcdef":
                            new_key = keys[:]
                            if grid[newr][newc] not in keys:
                                new_key = keys + grid[newr][newc]

                            if (newr, newc, new_key) not in visited:
                                visited.add((newr, newc, new_key))
                                q.append((newr, newc, new_key))

                        elif grid[newr][newc].lower() in keys and (newr, newc, keys) not in visited:
                            visited.add((newr, newc, keys))
                            q.append((newr, newc, str(keys)))

            steps += 1
                    
        return ans if ans != inf else -1