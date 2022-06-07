class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            # if amount == 0: return 0
            # def findmin(coins, amount, memo = {}):
            #     if amount in memo: return memo[amount]
            #     if amount == 0: return []
            #     if amount < 0: return None
            #     output = None
            #     for coin in coins:
            #         new = amount - coin
            #         res = findmin(coins, new)
            #         if res != None:
            #             res = res + [coin]
            #             if not output or len(res) < len(output):
            #                 output = res
            #     memo[amount] = output
            #     return output
            # minsize = findmin(coins,amount)
            # return len(minsize) if minsize else -1
        # now let's do this problem using tabulatio or bottom-up
        table = [-1]*(amount+1)
        table[0] = 0
        for i in range(len(table)):
            if table[i] != -1:
                for coin in coins:
                    index = i + coin
                    if index < len(table):
                        if table[index] == -1:
                            table[index] = table[i]+1
                        else:
                            new = table[i]+1
                            if table[index] > new:
                                table[index] = new
        return table[amount]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            