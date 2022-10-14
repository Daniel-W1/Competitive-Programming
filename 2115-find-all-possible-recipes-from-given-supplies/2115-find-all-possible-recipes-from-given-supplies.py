class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        for idx, recipe in enumerate(recipes):
            for ing in ingredients[idx]:
                graph[recipe].append(ing)
        
        not_made = set()
        supplies = set(supplies)
        def dfs(node):
            if node in supplies:
                return True
            
            if node in not_made:
                return False
            
            if node not in graph:
                return node in supplies
            
            not_made.add(node)
            for neigh in graph[node]:
                check = dfs(neigh)
                if not check:
                    return False
            
            not_made.remove(node)
            supplies.add(node)
            return True
        
        ans = []
        for recipe in recipes:
            check = dfs(recipe)
            if check:
                ans.append(recipe)
        
        return ans
        
        
            
            