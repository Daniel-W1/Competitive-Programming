class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # d = count(d)
        # r = count(r)
        # 3r, 3d
        # rdddrrdrdd
        #          |
        
        # rrrrdddd
        d, r = senate.count("D"), senate.count("R")
        killedR, killedD = 0, 0
        deleted = set()
        while d and r:
            for idx,letter in enumerate(senate):
                if idx in deleted: continue
                if letter == "R" and killedR == 0:
                    killedD += 1
                    d -= 1
                elif letter == "D" and killedD == 0:
                    killedR += 1
                    r -= 1
                elif letter == "R" and killedR > 0:
                    deleted.add(idx)
                    killedR -= 1
                else:
                    deleted.add(idx)
                    killedD -= 1

                if not r or not d:
                    return "Dire" if d else "Radiant"
        return "Dire" if d else "Radiant"