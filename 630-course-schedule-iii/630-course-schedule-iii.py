class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        maxheap = []
        runtime = 0
        courseCount = 0
        max_cnt = 0
        courses.sort(key = lambda c:c[1])
        for dur,last in courses:
            heapq.heappush(maxheap,-dur)
            runtime += dur
            if runtime <= last:
                courseCount += 1
            else:
                while runtime > last:
                    if runtime > last:
                        courseCount -= 1
                    runtime += heapq.heappop(maxheap)
                    
                if runtime <= last:
                    courseCount += 1
            max_cnt = max(max_cnt,courseCount)
        return max_cnt
                