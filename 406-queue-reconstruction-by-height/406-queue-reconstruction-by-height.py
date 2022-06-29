class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda val:val[0])
        # if the first value is smaller and if we can shift it
        # [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
        # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
        ans = [0]*len(people)
        for h,k in people:
            cnt = k
            pos = 0
            while cnt > 0 or isinstance(ans[pos],list):
                if ans[pos] == 0 or ans[pos][0] >= h:
                    cnt -= 1
                pos += 1
            ans[pos] = [h,k]
        return ans