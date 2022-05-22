class Solution:
    def intToRoman(self, num: int) -> str:
        all_map = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X" , 50:"L", 40:"XL",90:"XC",
                  100:"C",400:"CD",500:"D",1000:"M",900:"CM"}
        def convert(num, ans):
            if not num:
                return ans
            if num >= 1000:
                ans += all_map[1000]
                num -= 1000
                return convert(num, ans)
            elif num >= 900:
                ans += all_map[900]
                num -= 900
                return convert(num, ans)
            elif num >= 500:
                ans += all_map[500]
                num -= 500
                return convert(num, ans)
            elif num >= 400:
                ans += all_map[400]
                num -= 400
                return convert(num, ans)
            elif num >= 100:
                ans += all_map[100]
                num -= 100
                return convert(num, ans)
            elif num >= 90:
                ans += all_map[90]
                num -= 90
                return convert(num, ans)
            elif num >= 50:
                ans += all_map[50]
                num -= 50
                return convert(num, ans)
            elif num >= 40:
                ans += all_map[40]
                num -= 40
                return convert(num, ans)
            elif num >= 10:
                ans += all_map[10]
                num -= 10
                return convert(num, ans)
            elif num == 9:
                ans += all_map[9]
                num -= 9
                return convert(num, ans)
            elif num >= 5:
                ans += all_map[5]
                num -= 5
                return convert(num, ans)
            elif num == 4:
                ans += all_map[4]
                num -= 4
                return convert(num, ans)
            else:
                rec = "I"*num
                ans += rec
                num = 0
                return convert(num, ans)
        return convert(num, "")

            
            