
# Test cases
import unittest
from Grade import  add_grade, average_grade, highest_grade, lowest_grade
class TestStudent(unittest.TestCase):
    def test_add_grade_valid(self):
        student = Student("Alice")
        self.assertTrue(student.add_grade(85))
        self.assertIn(85, student.grades)

    def test_add_grade_invalid(self):
        student = Student("Bob")
        self.assertFalse(student.add_grade(105))
        self.assertNotIn(105, student.grades)

    def test_average_grade(self):
        student = Student("Charlie")
        student.add_grade(80)
        student.add_grade(90)
        self.assertEqual(student.average_grade(), 85)

    def test_highest_grade(self):
        student = Student("Diana")
        student.add_grade(70)
        student.add_grade(95)
        student.add_grade(85)
        self.assertEqual(student.highest_grade(), 95)

    def test_lowest_grade(self):
        student = Student("Eve")
        student.add_grade(60)
        student.add_grade(40)
        student.add_grade(75)
        self.assertEqual(student.lowest_grade(), 40)

    def test_average_grade_empty(self):
        student = Student("Frank")
        self.assertEqual(student.average_grade(), 0)

    def test_highest_grade_empty(self):
        student = Student("Grace")
        self.assertIsNone(student.highest_grade())

    def test_lowest_grade_empty(self):
        student = Student("Hank")
        self.assertIsNone(student.lowest_grade())

if __name__ == "__main__":
    unittest.main()
