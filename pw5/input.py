import math
import pickle
import numpy as np

class Student():
    def __init__(self,name ,id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student Name: ")
        self.__dob = input("Student DOB: ")

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dob(self):
        return self.__dob
    
    def __str__(self):
       print(f"Name: {self.__name} | ID: {self.__id} | DOB: {self.__dob}")

class Course():
    def __init__(self,id, name, credits):
        self.__id = id
        self.__name = name
        self.__credit = credits

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        self.__credit = input("Course Credits: ")
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit
    
    def __str__(self):
        print(f"Name: {self.__name} | ID: {self.__id} | Credits: {self.__credit}")
    
class Mark():
   def __init__(self, sid, cid, mark):
        self.sid = sid
        self.cid = cid
        self.mark = mark

   def __str__(self):
    return f"{self.sid} | {self.cid} | {self.mark} "
       
    
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

    def input_Course(self):
        n = int(input("Enter the number of course: "))
        for i in range(n):
            c = Course("", "", "")
            c.input()
            self.course.append(c)

            with open("course.txt", 'a') as d:
             d.write(str(c) + "\n")
        
            self.mark[c.get_id()] = []

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

    def average_gpa(self):
        self.gpa_list = []
        self.credit_list = []

        stu_id = input("Enter student id to get GPA: ")
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

        print(f"Average GPA of student {stu_id}: {math.floor(final_gpa)}")
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
    
    def save_all(self):
     data = {
        "students": self.students,
        "courses": self.course,
        "marks": self.mark
     }
     with open("students.dat", "wb") as f:
        pickle.dump(data, f)
     print("Saved all data → students.dat")

    def load_all(self):
     with open("students.dat", "rb") as f:
        data = pickle.load(f)
     self.students = data["students"]
     self.course = data["courses"]
     self.mark = data["marks"]
     print("Loaded data from students.dat")


    

    