class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            char = searchWord[i]
            filtered = []
            for word in products:
                if i < len(word) and word[i] == char:
                       filtered.append(word)
            level = []
            for i in range(len(filtered)):
                level.append(filtered[i])
                if i == 2:
                    break
            ans.append(level)
            products = filtered
        return ans
            
                