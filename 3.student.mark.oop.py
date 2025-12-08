import math
import numpy as np
import curses

# input function
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
    
    def display(self):
       print(f"Name: {self.__name} | ID: {self.__id} | DOB: {self.__dob}")
    
class Course():
    def __init__(self,id, name, credits):
        self.__id = id
        self.__name = name
        self.__credit = credits

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        self.__credit = int(input("Course Credits: "))
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit
    
    def display(self):
        print(f"Name: {self.__name} | ID: {self.__id} | Credits: {self.__credit}")
    
class Mark():
   def __init__(self, sid, cid, mark):
        self.sid = sid
        self.cid = cid
        self.mark = mark
    
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

    def display_Student(self):
        for s in self.students:
            s.display()

    def input_Course(self):
        n = int(input("Enter the number of course: "))
        for i in range(n):
            c = Course("", "", "")
            c.input()
            self.course.append(c)
            self.mark[c.get_id()] = []

    def display_Course(self):
        for c in self.course:
            c.display()

    def get_Mark(self):
       for c in self.course:
         c_id = c.get_id()
         
         print(f" --- Input mark for course {c_id} --- ")
         for stu in self.students:
            m = float(input(f"Enter mark for {stu.get_name()} ({stu.get_id()}): "))
           
            mark_s = Mark(stu.get_id(), c_id, (math.floor(m*10)/10) )
            self.mark[c_id].append(mark_s)

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
            gpa = self.gpa_values[i]
            print(f"Name: {stu.get_name()} | ID: {stu.get_id()} | GPA: {(math.floor(gpa*10)/10)} ")


def main():
    m = Mark_Management()
    m.input_student()
    m.display_Student()

    m.input_Course()
    m.display_Course()

    m.get_Mark()
    m.display_Mark()
    
    stu_id =input("Enter Student ID to get GPA: ")
    gpa = m.average_gpa(stu_id)
    print(f"GPA of {stu_id}: {(math.floor(gpa*10)/10)}")

    m.sort_gpa()

main()



    

    




    

    
    



