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
        for person in employees:
            if person.id == id:
                break
        self.ans = 0
        def dfs(person):
            self.ans += person.importance
            for p in person.subordinates:
                for sub in employees:
                    if sub.id == p:
                        break
                dfs(sub)
        dfs(person)
        return self.ans
                
                