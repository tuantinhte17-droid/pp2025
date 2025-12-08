import math
from domains.mark_management import Mark_Management

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
    print(f"GPA of Student with {stu_id}: {(math.floor(gpa*10)/10)}")

    m.sort_gpa()

main()