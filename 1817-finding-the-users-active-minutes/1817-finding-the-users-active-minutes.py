class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active_mins = defaultdict(set)
        
        for user_id, user_min in logs:
            active_mins[user_id].add(user_min)
        
        cnt = Counter([len(active_mins[user]) for user in active_mins])

        return [cnt[user_cnt] for user_cnt in range(1, k+1)]