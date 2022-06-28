class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = Counter(s).values()
        seen = set()
        deletion = 0
        for freq in freqs:
            while freq > 0 and freq in seen:
                deletion += 1
                freq -= 1
            seen.add(freq)
        return deletion
                
        