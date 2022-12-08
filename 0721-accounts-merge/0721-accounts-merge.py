class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        # rank = [1] * n
        parents = [idx for idx in range(n)]

        def find(index):
            while parents[index] != index:
                parents[index] = parents[parents[index]]
                index = parents[index]
            return index
        
        def union(index1, index2):
            parent1, parent2 = find(index1), find(index2)
            parents[parent1] = parent2
        
        # now do the n^2 part
        owners = {}
        for idx, account in enumerate(accounts):
            for idx2 in range(1, len(account)):
                email = account[idx2]
                
                if email in owners:
                    union(idx, owners[email])
                    
                owners[email] = idx
        
        # print(parents)
        merged = defaultdict(set)
        for idx, parent in enumerate(parents):
            for email in accounts[idx][1:]:
                merged[find(parent)].add(email)
        
        return [[accounts[idx][0]] + sorted(merged[idx]) for idx in merged]
        
                