class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for m in moves:
            if m == "U":
                pos[1]+= 1
            if m == "D":
                pos[1] -= 1
            if m == "R":
                pos[0] += 1
            if m == "L":
                pos[0] -= 1
        return pos == [0,0]