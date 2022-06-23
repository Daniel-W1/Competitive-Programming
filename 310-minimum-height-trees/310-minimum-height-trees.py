# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         def build_graph(edges):
#             graph = {}
#             for edge in edges:
#                 n1,n2 = edge[0],edge[1]
#                 if n1 not in graph:
#                     graph[n1] = []
#                 if n2 not in graph:
#                     graph[n2] = []
#                 graph[n1].append(n2)
#                 graph[n2].append(n1)
#             return graph
#         graph = build_graph(edges)
#         if not graph: return [0]
        
#         # for i in range(n):
#         #     for j in range(n):
#         #         if j in graph and i in graph and graph[j] == graph[i]:
#         #             graph.pop(j)
#         def dfs(node,visited):
#             if node in visited:
#                 return 0
#             ans = -float('inf')
#             visited.add(node)
#             for n in graph[node]:
#                 res = dfs(n,visited)+1
#                 ans = max(ans,res)
#             return ans
#         result = []
#         the_min = float('inf')
#         for node in graph:
#             visited = set()
#             if len(graph[node]) > 1:
#                 res = dfs(node,visited)
#             if len(visited) == len(graph):
#                 result.append((res,node))
#                 the_min = min(the_min,res)
#         return [node for res,node in result if res == the_min]
        
                
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves