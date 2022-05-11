class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1,1]]
        else:
            ans = [[1], [1,1]]
            for _ in range(n-2):
                l, h = 0, 1
                out = []
                while h < len(ans[-1]):
                    out.append(sum(ans[-1][l:h+1]))
                    l += 1
                    h += 1
                ans.append([1]+out+[1])
            return ans