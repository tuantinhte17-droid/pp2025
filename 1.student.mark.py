students = []
course = []
marks = {}

def student_info():
    id = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Student DoB: ")

    students.append({"id": id, "name": name, "dob": dob})

def number_of_students():
    n = int(input("Enter the number of students: "))
    for i in range(n):
        print(f"Enter the infomation for student {i+1} ")
        student_info()
    print("Finish")

def course_info():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")

        course.append({"course_id": c_id, "course_name": c_name})
        marks[c_id] = []

def input_mark():
    c_id = input("Enter course ID to get mark: ")

    if c_id not in [c['course_id'] for c in course]:
        print("Course not found ")
        return 

    for stu in students:
        m = float(input(f"Enter mark for {stu['name']} ({stu['id']}): "))
        marks[c_id].append({"Student_Id":stu['id'], "Mark":m})


def student_list():
    print("------ Students list -------- ")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']} ")

def course_list():
    print(" ------ Course list ------ ")
    for c in course:
        print(f"Course_ID: {c['course_id']}, Course_name: {c['course_name']} ")

def get_student_mark():
    c_id = input("Enter course ID to get the student's mark: ")
    if c_id not in marks:
        return
    
    print(f"--- Student mark for course {c_id} ---- ")
    for m2 in marks[c_id]:
        stu_id = m2["Student_Id"]
        # Tìm name dựa theo id
        stu_name = " "
        for s in students:
            if s["id"] == stu_id:
                stu_name = s["name"]
                break
        print(f"{stu_name} ({stu_id}) : {m2['Mark']}")


print("------- Student Mark Management ------ ")

number_of_students()
student_list()

course_info()
course_list()

input_mark()
get_student_mark()

print("END")









                  
      





