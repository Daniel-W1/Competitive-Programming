class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [val for val in range(n)]
        check_avail = {}
        
        cur_time = 0
        heapify(rooms)
        m = len(meetings)
        cnt = Counter()
        
        idx = 0
        
        while idx < m:
            
            for room in check_avail:
                if check_avail[room] != 10**9  and check_avail[room] <= cur_time:
                    heappush(rooms, room)
                    check_avail[room] = 10**9

            if rooms:
                cur_room = heappop(rooms)
                cur_time = max(cur_time, meetings[idx][0])
                check_avail[cur_room] = cur_time + meetings[idx][1] - meetings[idx][0]
                cnt[cur_room] += 1
                idx += 1
                
                if idx < m:
                    cur_time = max(cur_time, meetings[idx][0])
            else:
                cur_time = min(check_avail.values())
        
        # print(cnt)
        the_max = max(cnt.values())
        return [room for room in range(n) if cnt[room] == the_max][0]
        
            
        