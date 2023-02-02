class Solution:
    def convertThreeDigit(self, num: int) -> str:
        nums = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 
                'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                'Nineteen']
        tys = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
               'Eighty', 'Ninety']
        
        res = ''
        if num >= 100:
            res += nums[num//100] + ' Hundred'
            num = num%100
        
        if 1 <= num <= 19:
            if res:
                res += ' '
            res += nums[num]
        elif num >= 20:
            if res:
                res += ' '
            res += tys[(num-20)//10]
            num = (num-20)%10
            if num:
                res += ' ' + nums[num]
        
        return res if res else 'Zero'
    
    def numberToWords(self, num: int) -> str:
        if num >= 1000000000:
            res1 = self.convertThreeDigit(num//1000000000) + ' Billion'
            res2 = self.numberToWords(num%1000000000)
            return res1 + ' ' + res2 if res2 != 'Zero' else res1
        elif num >= 1000000:
            res1 = self.convertThreeDigit(num//1000000) + ' Million'
            res2= self.numberToWords(num%1000000)
            return res1 + ' ' + res2 if res2 != 'Zero' else res1
        elif num >= 1000:
            res1 = self.convertThreeDigit(num//1000) + ' Thousand'
            res2 = self.numberToWords(num%1000)
            return res1 + ' ' + res2 if res2 != 'Zero' else res1
        else:
            return self.convertThreeDigit(num)