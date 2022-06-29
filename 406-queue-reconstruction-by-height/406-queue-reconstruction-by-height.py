class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda pair : (-pair[0], pair[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue