class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        tree = defaultdict(list)
        
        for n1, n2 in roads:
            tree[n1].append(n2)
            tree[n2].append(n1)
        
        def dfs(node, parent):
            people, cost = 1, 0
            
            for child in tree[node]:
                if child != parent:
                    new_people, new_cost = dfs(child, node)
                    people += new_people
                    cost += new_cost
            
            cars = ceil(people/seats)
            
            # print(cars, people, cost, node, "here")
            return (people, cars + cost) if node != 0 else cost
    
        return dfs(0, 0)
    
                
        