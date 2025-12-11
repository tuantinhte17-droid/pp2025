import math
import numpy as np
from domains.student import Student
from domains.courses import Course
from domains.mark import Mark

class Mark_Management():
    def __init__(self):
      self.students = []
      self.course = []
      self.mark = {}

    def input_student(self):
        n = int(input("Enter the number of student: "))
        for i in range(n):
            s = Student("", "", "")
            s.input()
            self.students.append(s)
            with open("students.txt", 'a') as f:
               f.write(str(s) + "\n")

    def display_Student(self):
        for s in self.students:
            s.display()

    def input_Course(self):
        n = int(input("Enter the number of course: "))
        for i in range(n):
            c = Course("", "", "")
            c.input()
            self.course.append(c)

            with open("course.txt", 'a') as d:
               d.write(str(c) + "\n")

            self.mark[c.get_id()] = []

    def display_Course(self):
        for c in self.course:
            c.display()

    def get_Mark(self):
       c_id = input("Enter course ID to get mark: ")

       if c_id not in self.mark:
            print("Invalid Course ")
            return
        
       print(f" --- Input mark for course {c_id} --- ")
       for stu in self.students:
            m = float(input(f"Enter mark for {stu.get_name()} ({stu.get_id()}): "))
           
            mark_s = Mark(stu.get_id(), c_id, (math.floor(m*10)/10))
            self.mark[c_id].append(mark_s)
            with open("marks.txt", 'a') as n:
                n.write(str(mark_s) + "\n")
    
    def display_Mark(self):
        for c in self.course:
            c_id = c.get_id()
            print(f" -- Mark for {c_id} ---")
            for n in self.mark[c_id]:
               name = next((s.get_name() for s in self.students if s.get_id() == n.sid) , None)
               print(f"Student Name: {name} | Student ID:{n.sid} | Mark: {n.mark}")


    def average_gpa(self,stu_id):
        self.gpa_list = []
        self.credit_list = []
        for c in self.course:
            c_id = c.get_id()
            mark_s = next((m for m in self.mark[c_id] if m.sid == stu_id), None)
        
            if mark_s:
                self.gpa_list.append(mark_s.mark)
                self.credit_list.append(c.get_credit())
            
        if len(self.gpa_list) == 0:
            print("Student has no marks!!! ")
            return None
        
        gpa_arr = np.array(self.gpa_list)
        cre_arr = np.array(self.credit_list)

        weighted_sum = np.sum(gpa_arr * cre_arr)
        total_credit = np.sum(cre_arr)

        final_gpa = weighted_sum/total_credit
        return final_gpa
    
    
    def sort_gpa(self):
        self.gpa_values = []
        for stu in self.students:
            gpa = self.average_gpa(stu.get_id())
            self.gpa_values.append(gpa if gpa is not None else -1)

        gpa_arr = np.array(self.gpa_values)
        index = np.argsort((gpa_arr))[::-1]

        print("----- Students GPA sorted (descending): -----")
        for i in index:
            stu = self.students[i]
            print(f"{stu.get_name()} | ({stu.get_id()})")
