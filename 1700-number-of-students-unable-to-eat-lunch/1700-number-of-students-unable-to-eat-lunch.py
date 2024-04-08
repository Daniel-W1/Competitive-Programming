class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque([(val, 0) for val in students])
        sandwiches = sandwiches[::-1]
        
        while sandwiches:
            cur_student, from_back = students.popleft()
            
            if sandwiches[-1] == cur_student:
                sandwiches.pop()
            else:
                if not students or students[-1][1] > 10: return len(students) + 1
                students.append((cur_student, from_back + 1))
                        
        return len(students)