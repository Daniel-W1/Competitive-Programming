class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first_num = 0
        power = 0
        for i in range(len(a)-1, -1, -1):
            first_num += (2**(power)*int(a[i]))
            power +=  1
        second_num = 0
        power = 0
        for i in range(len(b)-1, -1, -1):
            second_num += (2**(power)*int(b[i]))
            power +=  1
        total = first_num + second_num
        print(first_num, second_num)
        binary = ""
        while total:
            binary += str((total%2))
            total //= 2
        return binary[::-1] if binary else "0"
            