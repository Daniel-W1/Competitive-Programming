class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for m in moves:
            if m == "U":
                pos[1]+= 1
            elif m == "D":
                pos[1] -= 1
            elif m == "R":
                pos[0] += 1
            else:
                pos[0] -= 1
        return pos == [0,0]