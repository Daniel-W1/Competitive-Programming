class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l,h = 0,len(products)-1
        ans = []
        for i,char in enumerate(searchWord):
            while l <= h and (i >= len(products[l]) or products[l][i] != char):
                l += 1
            while l <= h and (i >= len(products[h]) or products[h][i] != char):
                h -= 1
            cnt = 0
            level = []
            remain = h-l+1
            for j in range(min(3,remain)):
                level.append(products[l+j])
            ans.append(level)
        return ans
            