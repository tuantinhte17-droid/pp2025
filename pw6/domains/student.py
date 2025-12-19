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