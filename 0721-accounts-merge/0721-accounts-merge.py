class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        rank = [1] * n
        parents = [idx for idx in range(n)]

        def find(index):
            while parents[index] != index:
                parents[index] = parents[parents[index]]
                index = parents[index]
            return index
        
        def union(index1, index2):
            parent1, parent2 = find(index1), find(index2)
            
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                
            elif rank[parent1] < rank[parent2]:
                parents[parent1] = parent2
                
            else:
                parents[parent2] = parent1
                rank[parent1] += 1
                
        # now do the n^2 part
        for idx, account in enumerate(accounts):
            account1 = set(account[1:])
            for idx2 in range(n):
                account2 = set(accounts[idx2][1:])
                if account1 & account2:
                    union(idx, idx2)
        
        # print(parents)
        merged = defaultdict(set)
        for idx, parent in enumerate(parents):
            for email in accounts[idx][1:]:
                merged[find(parent)].add(email)
        
        return [[accounts[idx][0]] + sorted(merged[idx]) for idx in merged]
        
                