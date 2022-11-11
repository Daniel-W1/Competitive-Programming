class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % 1_000_000_007
            k += 1