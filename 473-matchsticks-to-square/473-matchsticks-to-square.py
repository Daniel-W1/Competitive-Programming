class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        # so what is the main thing that i need to check.
        if len(ms) < 4 or sum(ms) %2:
            return False
        memo = {}
        total = sum(ms)
        ms.sort(reverse = True)
        def construct(i, left, right, top, down):
            if (left, right,top,down) in memo: return memo[left,right,top,down]
            if i > len(ms)-1:
                return left == right == top == down
            the_max = max(top,down,right,left)
            new_total = top+down+right+left
            if (total)//4 < the_max:
                return False
            memo[left,right,top,down] = construct(i+1,left+ms[i], right, top, down) or construct(i+1 , left, right + ms[i], top, down) or construct(i+1,left, right, top + ms[i], down) or construct(i+1,left, right, top, down + ms[i])
            return memo[left,right,top,down]
        return construct(0,0,0,0,0)
        # now let's figure out the overlapping things to solve this things
        # 