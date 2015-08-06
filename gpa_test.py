import sys
import unittest
from gpa import *

class TestGPA(unittest.TestCase):

    def setUp(self):
        pass

    def test_round1(self):
        courses = [{'course' : 'Intro to Computer Science','grade' : 'A'},
         {'course' : 'Freshman Writing Seminar','grade' : 'A'},
         {'course' : 'Calculus I','grade' : 'B'},
         {'course' : 'Physics I','grade' : 'C'}]
        self.assertAlmostEqual(3.25,calculate(courses),5)

    def test_round2(self):
        courses = [{'course' : 'Intro to Philosophy','grade' : 'B-'},
         {'course' : 'Great Works of American Literature','grade' : 'A-'},
         {'course' : 'Calculus II','grade' : 'B+'},
         {'course' : 'Native American History I','grade' : 'A+'}]
        self.assertAlmostEqual(3.425,calculate(courses),5)

    def test_round3(self):
        courses = [{'course' : 'Welcome to the University','grade' : 'A','credits': 1},
         {'course' : 'Introduction to Sociology','grade' : 'A-','credits': 3},
         {'course' : 'Film Art in a Global Society','grade' : 'B+','credits': 4},
         {'course' : 'International Government','grade' : 'C','credits': 3}]
        self.assertAlmostEqual(3.11818,calculate(courses),4)

if __name__ == '__main__':
    unittest.main()
