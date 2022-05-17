class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
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
        binary = ""
        while total:
            binary += str((total%2))
            total //= 2
        return binary[::-1] if binary else "0"
        '''
        i = len(a)-1
        j = len(b)-1
        carry = 0
        binary = ""
        while i >= 0 and j >= 0:
            if a[i] == b[j] == "1" and not carry:
                binary += "0"
                carry = 1
            elif a[i] == b[j] == "1" and carry:
                binary += "1"
                carry = 1
            else:
                if a[i] != b[j] and not carry:
                    binary += "1"
                elif a[i] != b[j] and carry:
                    binary += "0"
                    carry = 1
                elif a[i]==b[j]=="0" and carry:
                    print(True)
                    binary += "1"
                    carry = 0
                else:
                    binary += "0"
            i -= 1
            j -= 1
        while i >= 0:
            if a[i] == "0":
                if carry:
                    binary += "1"
                    carry = 0
                else:
                    binary += "0"
            else:
                if carry:
                    binary += "0"
                    carry = 1
                else:
                    binary += "1"
            i -= 1
        while j >= 0:
            print(j)
            if b[j] == "0":
                if carry:
                    binary += "1"
                    carry = 0
                else:
                    binary += "0"
            else:
                if carry:
                    binary += "0"
                    carry = 1
                else:
                    binary += "1"
            j -= 1
        while carry:
            binary += str(carry)
            carry = 0
        return binary[::-1]
            
        