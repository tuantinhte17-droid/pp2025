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
    
    def display(self):
        print(f"Name: {self.__name} | ID: {self.__id} | Credits: {self.__credit}")