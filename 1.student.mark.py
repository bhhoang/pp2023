# student_info = dict.fromkeys(['student_id', 'name', 'dob', 'courses'], [])
# course_info = dict.fromkeys(['course_id', 'course_name', 'course_mark'], [])
list_of_students: list[dict] = list()
list_of_course: list[dict] = list()


def student_info(student_id: str, name: str, dob: str, courses: list) -> dict:
    """
    :param student_id: student ID
    :param name: student name
    :param dob: student date of birth
    :param courses: list of courses
    :return: student information as a dictionary
    """
    keys: list[str] = ["student_id", "name", "dob", "courses"]
    student_info: dict[str] = dict.fromkeys(keys, [])
    student_info["student_id"] = student_id
    student_info["name"] = name
    student_info["dob"] = dob
    student_info["courses"] = courses
    return student_info


def course_info(
    course_id: str,
    course_name: str,
    course_mark: float,
    ects: int,
    enrolled_student: list[str] = [],
) -> dict:
    """
    :param course_id: course ID
    :param course_name: course name
    :param course_mark: course mark
    :param ects: course ECTS
    :param enrolled_student: list of enrolled students id
    :return: course information as a dictionary
    """
    course_info = dict.fromkeys(
        ["course_id", "course_name", "course_mark", "ects", "enrolled_student"], []
    )
    course_info["course_id"] = course_id
    course_info["course_name"] = course_name
    course_info["course_mark"] = course_mark
    course_info["ects"] = ects
    course_info["enrolled_student"] = enrolled_student
    return course_info


def input_info() -> bool:
    n = int(input("Enter number of students: "))
    for i in range(n):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        courses = []
        m = int(input("Enter number of courses: "))
        for j in range(m):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course_mark = float(input("Enter course mark: "))
            ects = int(input("Enter course ECTS: "))
            courses.append(course_info(course_id, course_name, course_mark, ects))
        list_of_students.append(student_info(student_id, name, dob, courses))
    return True


def remove_student(student_id: str) -> bool:
    for student in list_of_students:
        if student["student_id"] == student_id:
            list_of_students.remove(student)
            return True
    print("Student ID not found")
    return False


def course_enroll(student_id: str, course_id: str) -> bool:
    for course in list_of_course:
        if course["course_id"] == course_id:
            course["enrolled_student"].append(student_id)
    for student in list_of_students:
        if student["student_id"] == student_id:
            for course in student["courses"]:
                if course["course_id"] == course_id:
                    print("Duplicate course ID")
                    return False
            course_name = input("Enter course name: ")
            course_mark = float(input("Enter course mark: "))
            ects = int(input("Enter course ECTS: "))
            student["courses"].append(
                course_info(course_id, course_name, course_mark, ects)
            )
    print("Student ID not found")
    return False


def course_unenroll(student_id: str, course_id: str) -> bool:
    for course in list_of_course:
        if course["course_id"] == course_id:
            course["enrolled_student"].remove(student_id)
    for student in list_of_students:
        if student["student_id"] == student_id:
            for course in student["courses"]:
                if course["course_id"] == course_id:
                    student["courses"].remove(course)
                    return True
            print("Course ID not found")
            return False
    print("Student ID not found")
    return False


def add_course(
    course_id: str,
    course_name: str,
    course_mark: float,
    ects: int,
    list_students: list[str] = [],
) -> bool:
    for course in list_of_course:
        if course["course_id"] == course_id:
            print("Duplicate course ID")
            return False
    list_of_course.append(
        course_info(course_id, course_name, course_mark, ects, list_students)
    )
    return True


def remove_course(course_id: str) -> bool:
    for course in list_of_course:
        if course["course_id"] == course_id:
            list_of_course.remove(course)
            return True
    print("Course ID not found")
    return False


def inspect_student(student_id: str) -> bool:
    for student in list_of_students:
        if student["student_id"] == student_id:
            print("+" + "-" * 50 + "+")
            print("| Student ID: " + student["student_id"])
            print("| Name: " + student["name"])
            print("| Date of Birth: " + student["dob"])
            print("+" + "-" * 50 + "+")
            for course in student["courses"]:
                print("|")
                print(f"+----Course Name: {course['course_name']}")
                print("|\t|")
                print(f"|\t+----Course ID: {course['course_id']}")
                print("|\t|")
                print(f"|\t+----Course Mark: {course['course_mark']}", end="")
            return True
    print("Student ID not found")
    return False


def inspect_course(course_id: str) -> bool:
    for course in list_of_course:
        if course["course_id"] == course_id:
            print("+" + "-" * 50 + "+")
            print("| Course ID: " + course["course_id"])
            print("| Course Name: " + course["course_name"])
            print("| Course Mark: " + course["course_mark"])
            print("| ECTS: " + course["ects"])
            print("+" + "-" * 50 + "+")
            for student in course["enrolled_student"]:
                print("|")
                print(f"+----Student ID: {student['student_id']}")
                print("|\t|")
                print(f"|\t+----Student Name: {student['name']}")
                print("|\t|")
                print(f"|\t+----Student DOB: {student['dob']}", end="")
            return True


def inspect_all_student() -> bool:
    for student in list_of_students:
        print("+" + "-" * 50 + "+")
        print("| Student ID: " + student["student_id"])
        print("| Name: " + student["name"])
        print("| Date of Birth: " + student["dob"])
        print("+" + "-" * 50 + "+")
        for course in student["courses"]:
            print("|")
            print(f"+----Course Name: {course['course_name']}")
            print("|\t|")
            print(f"|\t+----Course ID: {course['course_id']}")
            print("|\t|")
            print(f"|\t+----Course Mark: {course['course_mark']}", end="")
        print("\n\n")
    return True


def inspect_all_course() -> bool:
    for course in list_of_course:
        print("+" + "-" * 50 + "+")
        print("| Course ID: " + course["course_id"])
        print("| Course Name: " + course["course_name"])
        print("| Course Mark: " + course["course_mark"])
        print("| ECTS: " + course["ects"])
        print("+" + "-" * 50 + "+")
        for student in course["enrolled_student"]:
            print("|")
            print(f"+----Student ID: {student['student_id']}")
            print("|\t|")
            print(f"|\t+----Student Name: {student['name']}")
            print("|\t|")
            print(f"|\t+----Student DOB: {student['dob']}", end="")
        print("\n\n")
    return True


def main():
    choice = [
        "1. Add student",
        "2. Remove student",
        "3. Enroll course",
        "4. Unenroll course",
        "5. Add course",
        "6. Remove course",
        "7. Inspect student",
        "8. Inspect course",
        "9. Inspect all student",
        "10. Inspect all course",
        "11. Exit",
    ]
    while True:
        for i in choice:
            print(i)
        option = int(input("Enter your choice: "))
        if option == 1:
            input_info()
        elif option == 2:
            remove_student(input("Enter student ID: "))
        elif option == 3:
            course_enroll(input("Enter student ID: "), input("Enter course ID: "))
        elif option == 4:
            course_unenroll(input("Enter student ID: "), input("Enter course ID: "))
        elif option == 5:
            add_course(
                input("Enter course ID: "),
                input("Enter course name: "),
                float(input("Enter course mark: ")),
                int(input("Enter course ECTS: ")),
            )
        elif option == 6:
            remove_course(input("Enter course ID: "))
        elif option == 7:
            inspect_student(input("Enter student ID: "))
        elif option == 8:
            inspect_course(input("Enter course ID: "))
        elif option == 9:
            inspect_all_student()
        elif option == 10:
            inspect_all_course()
        elif option == 11:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
