class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [[etime, ptime, idx] for idx, (etime, ptime) in enumerate(tasks)]
        
        tasks.sort()
        
        cur_time = min(tasks, key = lambda triple: triple[0])[0]
        
        start_idx = 0
        
        heap = []
        ans = []

        # print(tasks)
        
        while len(ans) < len(tasks):
            if not heap and cur_time < tasks[start_idx][0]:
                cur_time = tasks[start_idx][0]
                
            while start_idx < len(tasks) and tasks[start_idx][0] <= cur_time:
                task = tasks[start_idx]
                heappush(heap, [task[1], task[2]])
                start_idx += 1
            
            ptime, idx = heappop(heap)
            ans.append(idx)
            cur_time += ptime

        return ans