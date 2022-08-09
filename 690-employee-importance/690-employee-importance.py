"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {node.id : (node.importance, node.subordinates) for node in employees}
        def calculate(person):
            if not person[1]:
                return person[0]
            answer = 0
            for subs in person[1]:
                answer += calculate(graph[subs])
            return answer + person[0]
        
        return calculate(graph[id])
            