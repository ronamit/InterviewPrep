
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        emp_per_id = {}
        for e in employees:
            emp_per_id[e.id] = e
        
        def sum_importances(i: int):
            e = emp_per_id[i]
            total = e.importance
            for child_id in e.subordinates:
                total += sum_importances(child_id)
            return total
        
        return sum_importances(id)
        