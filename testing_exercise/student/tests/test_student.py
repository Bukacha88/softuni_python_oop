from unittest import TestCase, main

from exam_prep.python_oop_exam_preparation_2_april_2020.project import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Test1')
        self.student_2 = Student('Test2', {'OOP': ['Solid', 'Testing']})

    def test_student__init_when_courses_is_None(self):
        self.assertEqual('Test1', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student__init_when_courses_is_not_None(self):
        self.assertEqual('Test2', self.student_2.name)
        self.assertEqual({'OOP': ['Solid', 'Testing']}, self.student_2.courses)

    def test_student_enroll__when_course_name_in_courses_and_no_add_course_notes(self):
        msg = "Course already added. Notes have been updated."
        self.assertEqual(msg, self.student_2.enroll('OOP', ['Patterns', 'Exam']))
        self.assertEqual({'OOP': ['Solid', 'Testing', 'Patterns', 'Exam']}, self.student_2.courses)

    def test_student_enroll__when_course_name_not_in_courses_and_add_course_notes(self):
        msg = "Course and course notes have been added."
        self.assertEqual(msg, self.student_2.enroll('Advanced', ['Lists', 'Functions']))
        self.assertEqual({'OOP': ['Solid', 'Testing'], 'Advanced': ['Lists', 'Functions']}, self.student_2.courses)

    def test_student_enroll__when_course_name_not_in_courses_and_Y_add_course_notes(self):
        msg = "Course and course notes have been added."
        self.assertEqual(msg, self.student.enroll('Advanced', ['Lists', 'Functions'], 'Y'))
        self.assertEqual({'Advanced': ['Lists', 'Functions']}, self.student.courses)

    def test_student_enroll__when_course_name_not_in_courses__and_N_add_course_notes(self):
        msg = "Course has been added."
        self.assertEqual(msg, self.student_2.enroll('Advanced', ['Lists', 'Functions'], 'N'))
        self.assertEqual({'OOP': ['Solid', 'Testing'], 'Advanced': []}, self.student_2.courses)

    def test_student_add_notes__when_course_name_in_courses(self):
        msg = "Notes have been updated"
        self.assertEqual(msg, self.student_2.add_notes('OOP', 'lists'))
        self.assertEqual({'OOP': ['Solid', 'Testing', 'lists']}, self.student_2.courses)

    def test_student_add_notes__when_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as context:
            self.student_2.add_notes('Advanced', 'lists')
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_student_leave_course__when_course_name_in_courses(self):
        msg = "Course has been removed"
        self.assertEqual(msg, self.student_2.leave_course('OOP'))
        self.assertEqual({}, self.student_2.courses)

    def test_student_leave_course__when_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as context:
            self.student_2.leave_course('Advanced')
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_student_methods(self):
        self.student_2.enroll('OOP', ['Patterns', 'Exam'], 'N')
        self.assertEqual({'OOP': ['Solid', 'Testing', 'Patterns', 'Exam']}, self.student_2.courses)
        self.student_2.add_notes('OOP', 'lists')
        self.assertEqual({'OOP': ['Solid', 'Testing', 'Patterns', 'Exam', 'lists']}, self.student_2.courses)
        self.student_2.leave_course('OOP')
        self.assertEqual({}, self.student_2.courses)


if __name__ == '__main__':
    main()
