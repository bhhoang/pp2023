import os

# Blueprint for a course
class Course:
    def __init__(self, courseID:str, courseName:str, courseMark:str, studentID:str):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__studentList = []
        self.__studentList.append([studentID,courseMark])

    def _getCourseID(self):
        return self.__courseID

    def _getCourseName(self):
        return self.__courseName

    def _getCourseMark(self, stuID:str):
        for student in self.__studentList:
            if student[0] == stuID:
                return student[1]
            
    def _getListMark(self):
        return self.__studentList

    def setCourseMark(self, stuID, courseMark):
        if not any(stuID in sublist for sublist in self.__studentList):
            return None
        else:
            for student in self.__studentList:
                if student[0] == stuID:
                    student[1] = courseMark

    def addStudent(self, studentID, courseMark):
        self.__studentList.append([studentID,courseMark])

# Any person has these
class Person:
    def __init__(self,name:str ,dob:str):
        self.__name = name
        self.__dob = dob
    def _getName(self):
        return self.__name
    def _getDob(self):
        return self.__dob
    def setName(self, name):
            self.__name = name
    def setDob(self, dob):
            self.__dob = dob

# Blueprint for a students
class Student(Person):
    def __init__(self, stuID:str, name:str, dob:str, Course:Course):
        super().__init__(name,dob)                
        self.__stuID = stuID
        self.__courseList = []
        self.__courseList.append(Course)
    def _getStuID(self):
        return self.__stuID
    def _getCourseList(self):
        return self.__courseList
    def addCourse(self, courseList):
        self.__courseList = self.__courseList.append(courseList)
    def setStuID(self, stuID):
        self._stuID = stuID
    def _getLastMark(self):
        return self.__courseList[-1]._getCourseMark(self.__stuID)

#Load saved data
def loadData():
    delimiter = "," if check_for_Delimiter() == False else check_for_Delimiter()
    studentList = []
    with open("./student.csv", "r") as f:
        f.readline()
        for line in f:
            args = line.split(delimiter)
            #remove the \n at the end of the line
            args[5] = args[5][:-1]
            if args[0] == "Student ID":
                continue
            stuID = args[0]
            name = args[1]
            dob = args[2]
            courseId = args[3]
            courseName = args[4]
            courseMark = args[5]
            studentList.append(Student(stuID, name, dob, Course(courseId, courseName, courseMark,stuID)))

    return studentList

#This function actually get and return both name and date of birth
def getPerCSV(stuID:str, delimiter:str = ","):
    if(os.path.exists("./student.csv") == False):
        return None
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            if args[0] == stuID:
                return args[1], args[2]
    return None

#Check duplicate course
def dupcourseCheck(stuID:str, courseId:str, delimiter:str = ","):
    if(os.path.exists("./student.csv") == False):
        return False
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            if args[0] == stuID and args[3] == courseId:
                return True
    return False

# Single input student block
def input_info():
    courseId, courseName, stuID, courseMark = "","","",""
    stuID = input("Enter student ID: ")
    delimiter = "," if check_for_Delimiter() == False else check_for_Delimiter()
    if checkDuplicate(stuID):
        name,dob = getPerCSV(stuID)
        courseId = input("Enter course ID: ")
        while dupcourseCheck(stuID,courseId,delimiter):
            print("Duplicate course ID")
            courseId = input("Re-enter course ID: ")
        courseName = input("Enter course name: ")
        courseMark = input("Enter course mark: ")
        return Student(stuID, name, dob, Course(courseId, courseName, courseMark,stuID))
    else:
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        courseId = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        courseMark = input("Enter course mark: ")
        return Student(stuID, name, dob, Course(courseId, courseName, courseMark,stuID))
    
#Check delimiter in file
def check_for_Delimiter():
    if(os.path.exists("./student.csv")):
        with open("./student.csv", "r") as f:
            line = f.readline()
            idx1 = line.find("Student ID")
            idx2 = line.find("Name")
            if idx1 != -1 and idx2 != -1:
                idx1 = idx1 + len("Student ID")
                return line[idx1:idx2].strip()
            else:
                return False
    else:
        return False

#Check duplicate student
def checkDuplicate(stuID:str, delimiter:str = ","):
    if(os.path.exists("./student.csv") == False):
        return False
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            if args[0] == stuID:
                return True
    return False


#Get the longest length of string in each column
def lookforLongest(delimiter:str = ","):
    longest = [0,0,0,0,0,0]
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            for i in range(len(longest)):
                if len(args[i]) > longest[i]:
                    longest[i] = len(args[i])
    return longest

#Serial input like since the practical asked for it
def serial_input(n:int):
    list_of_students = []
    delimiter = "," if check_for_Delimiter() == False else check_for_Delimiter()
    for i in range(n):
        stdInstace = input_info()
        list_of_students.append([stdInstace._getStuID(), stdInstace._getName(), stdInstace._getDob(), stdInstace._getCourseList()[-1]._getCourseID(), stdInstace._getCourseList()[-1]._getCourseName(), stdInstace._getLastMark()])
        write_info(list_of_students[i][1], list_of_students[i][0], list_of_students[i][2], list_of_students[i][3], list_of_students[i][4], list_of_students[i][5], delimiter)

#Write to file student.csv
def write_info(name:str, stuID:str, dob:str,courseID:str, courseName:str, courseMark:str, delimiter:str = ","):
    if(os.path.exists("./student.csv")):
        with open("./student.csv", "a") as f:
            ls = [stuID, name, dob,courseID,courseName,courseMark]
            f.write(delimiter.join(ls) + "\n")
    else:
        print("File students.csv not found in current working directory, creating one...")
        with open("./student.csv", "w") as f:
            ls = ["Student ID", "Name", "Date of Birth","Course ID","Course Name","Course Mark"]
            f.write(delimiter.join(ls)+ "\n")
            ls = [stuID, name, dob,courseID,courseName, courseMark]
            f.write(delimiter.join(ls) + "\n")

#Drawing the table
def disp(delimiter:str = ","):
    print("\n\n\n")
    if(os.path.exists("./student.csv")):
        longest = lookforLongest()
        with open("./student.csv", "r") as f:
            first_line = f.readline()
            args = first_line.split(delimiter)
            #remove the newline character
            args[5] = args[5][:-1]
            print("+ "+"-"*(longest[0]+longest[1]+longest[2]+longest[3]+longest[4]+longest[5]+39)+" +")
            print ("| " + args[0].ljust(longest[0]+4) + " | " + args[1].ljust(longest[1]+4) + " | " + args[2].ljust(longest[2]+4)+ " | " + args[3].ljust(longest[3]+4) + " | " + args[4].ljust(longest[4]+4)+" | " + args[5].ljust(longest[5]+4) + " |")
            print ("+ " + "-"*(longest[0]+4) + " + " + "-"*(longest[1] + 4) + " + " + "-"*(longest[2]+4) + " + " + "-"*(longest[3]+4) + " + " + "-"*(longest[4]+4)+ " + " + "-"*(longest[5]+4)+" +")
            for line in f:
                args = line.split(delimiter)
                #draw table border and datas
                args[5] = args[5][:-1]
                print ("| " + args[0].ljust(longest[0]+4) + " | " + args[1].ljust(longest[1]+4) + " | " + args[2].ljust(longest[2]+4)+ " | " + args[3].ljust(longest[3]+4) + " | " + args[4].ljust(longest[4]+4)+" | "+ args[5].ljust(longest[5]+4)+" |")
                print("+ "+"-"*(longest[0]+longest[1]+longest[2]+longest[3]+longest[4]+longest[5]+39)+" +")
    else:
        print("File students.csv not found in current working directory, creating one...")
        with open("./student.csv", "w") as f:
            ls = ["Student ID", "Name", "Date of Birth","Course ID", "Course Name", "Course Mark"]
            f.write(delimiter.join(ls)+ "\n")
    print("\n\n\n")


#Inspecting student's info and courses mark
def inspectStudent(stuID:str):
    print("\n\n\n")
    stuLis = loadData()
    for student in stuLis:
        if student._getStuID() == stuID:
            name = student._getName()
            dob = student._getDob()
    print("+"+"-"*50+"+")
    print("| Student ID: " + stuID)
    print("| Name: " + name )
    print("| Date of Birth: " + dob)
    print("+"+"-"*50+"+")
    for student in stuLis:
        if student._getStuID() == stuID:
            name = student._getName()
            dob = student._getDob()
            for course in student._getCourseList():
                print("|")
                print(f"+----Course Name: {course._getCourseName()}")
                print("|\t|")
                print(f"|\t+----Course ID: {course._getCourseID()}")
                print("|\t|")
                print(f"|\t+----Course Mark: {course._getCourseMark(stuID)}")
    print("\n\n\n")

#Interface
def main():
    delimiter = check_for_Delimiter() if check_for_Delimiter() else ","
    choice = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students","Remove data" ,"Inspect Student", "Exit"]
    yn = "y"
    while(yn == "y"):
        for i in range(len(choice)):
            print(f"{i+1}. {choice[i]}")
        print("Please choose an option: ", end="")
        option = input()
        if(option == "1"):
            stdInstance = input_info()
            lastCourse = (stdInstance._getCourseList())[-1]
            stuID = stdInstance._getStuID()[:]
            write_info(stdInstance._getName(), stdInstance._getStuID(), stdInstance._getDob(), lastCourse._getCourseID(), lastCourse._getCourseName(), lastCourse._getCourseMark(stdInstance._getStuID()), delimiter)
        elif(option == "2"):
            disp(delimiter)
        elif(option == "3"):
            if(check_for_Delimiter()):
                delimiter = check_for_Delimiter()
                print(f"The student file has already got delimiter which is {delimiter}")
            else:
                delimiter = input("Please input the delimiter (default is ,): ")
        elif(option == "4"):
            amount = int(input("Please input the amount of students: "))
            serial_input(amount)
        elif(option == "5"):
            if os.path.exists("./student.csv"):
                os.remove("./student.csv")
                print("The file has been removed!")
            else:
                print("The file does not exist!")
        elif(option == "6"):
            stuID = input("Please input the student ID: ")
            inspectStudent(stuID)
        elif(option == "7"):
            yn = "n"
        else:
            print("Invalid option")

if __name__ == "__main__":
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to the student management system!")
        main()
    except KeyboardInterrupt:
        print("\nProgram has been terminated!")
    finally:
        print("Program exited!")

