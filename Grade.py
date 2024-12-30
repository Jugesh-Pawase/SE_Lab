class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

    def lowest_grade(self):
        if not self.grades:
            return None
        return min(self.grades)
