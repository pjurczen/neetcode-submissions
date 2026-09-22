class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_counts: dict[int, int] = {0: 0, 1: 0}
        for s in students:
            student_counts[s] += 1

        for s in sandwiches:
            if student_counts[s] > 0:
                student_counts[s] -= 1
            else:
                break
        return student_counts[0] + student_counts[1]

            
        
