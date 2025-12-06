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
    def __init__(self,id, name):
        self.__id = id
        self.__name = name

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    
    def display(self):
        print(f"Name: {self.__name} | ID: {self.__id}")
    
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
            c = Course("", "")
            c.input()
            self.course.append(c)
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

            mark_s = Mark(stu.get_id(), c_id, m)
            self.mark[c_id].append(mark_s)

    def display_Mark(self):
        c_id = input("Enter the course ID to get Mark: ")
        if c_id not in self.mark:
            print("Error")
            return
        
        print(f" -- Mark for {c_id} ---")
        for n in self.mark[c_id]:
            name = next((s.get_name() for s in self.students if s.get_id() == n.sid) , None)
            print(f"Student Name: {name} | Student ID:{n.sid} : {n.mark}")
        

def main():
    m = Mark_Management()
    m.input_student()
    m.display_Student()

    m.input_Course()
    m.display_Course()

    m.get_Mark()
    m.display_Mark()

main()



    

    




    

    
    



