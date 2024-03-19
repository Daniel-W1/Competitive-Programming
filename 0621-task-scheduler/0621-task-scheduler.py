class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
             ["A","A","A", "B","B","B"],
             
             {
                "A": 3,
                "B": 3
             }
        """
        cnt = Counter(tasks)
        pos_and_cnt = [(-cnt[val], -1) for val in cnt.keys()]
        waiting_q = deque([])
        
        heapify(pos_and_cnt)
                
        current_idx = 0
        ans = 0
        
        while pos_and_cnt or waiting_q:
            while waiting_q and current_idx - waiting_q[0][1] > n:
                heappush(pos_and_cnt, waiting_q.popleft())
            
            if pos_and_cnt:
                count, idx = heappop(pos_and_cnt)
                if count + 1:
                    waiting_q.append((count + 1, current_idx))
        
            ans += 1
            current_idx += 1
        
        return ans