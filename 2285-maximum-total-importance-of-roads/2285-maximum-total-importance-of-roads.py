class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = [0 for _ in range(n)]
        for a, b in roads:
            cnt[a] += 1
            cnt[b] += 1
        cnt.sort(reverse = True)
        ans = 0
        w = n
        for c in cnt:
            if c == 0:
                break
            ans += c*w
            w -= 1
        return ans