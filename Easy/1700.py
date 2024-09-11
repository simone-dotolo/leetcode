class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        new = 0
        old = len(students)

        while new != old:
            old = len(students)
            i = 0
            j = 0
            while j < len(students):
                if students[j] == sandwiches[i]:
                    students.pop(j)
                    sandwiches.pop(i)
                else:
                    j += 1
            new = len(students)
        
        print(students, sandwiches)

        return len(students)