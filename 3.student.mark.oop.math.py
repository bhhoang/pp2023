import os
import math
import numpy as np

import curses
from curses import wrapper
from curses import panel

## Define some variable
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
stdscr.keypad( 1 )
stdscr.border( 0 )
curses.curs_set( 0 )
choices = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students","Remove data" ,"Inspect Student", "Print GPA List", "GPA of a student", "Exit"]
max_row = len(choices)
box = curses.newwin( max_row + 2, 64, 1, 1 )
box.box()
position = 1
row_num = len(choices)

# Blueprint for a course
class Course:
    __studentList = []
    def __init__(self, courseID, courseName, courseMark, studentID):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__studentList.append([studentID,courseMark])
    def _getCourseID(self):
        return self.__courseID

    def _getCourseName(self):
        return self.__courseName

    def _getCourseMark(self, stuID):
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
        if not any(studentID in sublist for sublist in self.__studentList):
            self.__studentList.append([studentID,courseMark])
        else:
            return None

# Blueprint for a students
class Student:
        __courseList = []
        def __init__(self, stuID:str, name:str, dob:str, Course:Course):
            self.__stuID = stuID
            self.__name = name
            self.__dob = dob
            self.__courseList.append(Course)
        def _getStuID(self):
            return self.__stuID
        def _getName(self):
            return self.__name
        def _getDob(self):
            return self.__dob
        def _getCourseList(self):
            return self.__courseList
        def addCourse(self, courseList):
            self.__courseList = self.__courseList.append(courseList)
        def setStuID(self, stuID):
            self._stuID = stuID
        def setName(self, name):
            self.__name = name
        def setDob(self, dob):
            self.__dob = dob
        def _GPA(self):
            GPA = 0
            for i in range(len(self.__courseList)):
                GPA = GPA + (self.__courseList[i])._getCourseMark(self.__stuID)
            GPA = GPA/len(self.__courseList)
            return GPA
#This function actually get and return both name and date of birth
def getName(stuID:str, delimiter:str = ","):
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
        name,dob = getName(stuID)
        courseId = input("Enter course ID: ")
        while dupcourseCheck(stuID,courseId,delimiter):
            print("Duplicate course ID")
            courseId = input("Re-enter course ID: ")
        courseName = input("Enter course name: ")
        courseMark = float(input("Enter course mark: "))
        courseMark = math.floor(courseMark)
        courseMark = str(courseMark)
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

#Load into object
def load_into_object():
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
def consecutive_input(n:int):
    list_of_students = []
    delimiter = "," if check_for_Delimiter() == False else check_for_Delimiter()
    for i in range(n):
        stuID, name, dob, courseId, courseName, courseMark = input_info()
        list_of_students.append([stuID, name, dob, courseId, courseName, courseMark])
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
def inspectStudent(stuID:str, delimiter:str = ","):
    print("\n\n\n")
    stuLis = load_into_object()
    if(os.path.exists("./student.csv")):
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
                    print(f"|\t+----Course Mark: {course._getCourseMark(stuID)}", end="")
    print("\n\n\n")


def getAllStuID():
    stuIDs = []
    studentList = load_into_object()
    for student in studentList:
        if(student._getStuID() not in stuIDs):
            stuIDs.append(student._getStuId())
    return stuIDs

def evalListGPA():
    stuIDs = getAllStuID()
    gpaList = []
    for stuID in stuIDs:
        gpaList.append([stuID, evalGPA(stuID)])
    #sort the list by gpa
    gpaList.sort(key=lambda x: x[1], reverse=True)
    return gpaList

def printGPAList():
    gpaList = evalListGPA()
    print("\n\n\n")
    print("+"+"-"*38+"+")
    print("| Student ID\t| GPA ")
    print("+"+"-"*38+"+")
    for stuID, gpa in gpaList:
        print(f"| {stuID}\t| {gpa}")
    print("+"+"-"*38+"+")
    print("\n\n\n")

#Interface
#def main():
#    delimiter = check_for_Delimiter() if check_for_Delimiter() else ","
#    choice = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students","Remove data" ,"Inspect Student", "Print GPA List", "GPA of a student", "Exit"]
#    yn = "y"
#    while(yn == "y"):
#        for i in range(len(choice)):
#            print(f"{i+1}. {choice[i]}")
#        print("Please choose an option: ", end="")
#        option = input()
#        if(option == "1"):
#            stdInstance = input_info()
#            lastCourse = (stdInstance._getCourseList())[-1]
#            write_info(stdInstance._getName(), stdInstance._getStuID(), stdInstance._getDob(), lastCourse._getCourseID(), lastCourse._getCourseName(), lastCourse._getCourseMark(stdInstance._getStuID()), delimiter)
#        elif(option == "2"):
#            disp(delimiter)
#        elif(option == "3"):
#            if(check_for_Delimiter()):
#                delimiter = check_for_Delimiter()
#                print(f"The student file has already got delimiter which is {delimiter}")
#            else:
#                delimiter = input("Please input the delimiter (default is ,): ")
#        elif(option == "4"):
#            amount = int(input("Please input the amount of students: "))
#            consecutive_input(amount)
#        elif(option == "5"):
#            if os.path.exists("./student.csv"):
#                os.remove("./student.csv")
#                print("The file has been removed!")
#            else:
#                print("The file does not exist!")
#        elif(option == "6"):
#            stuID = input("Please input the student ID: ")
#            inspectStudent(stuID, delimiter)
#        elif(option == "7"):
#            printGPAList()
#        elif(option == "8"):
#            yn = "n"
#        else:
#            print("Invalid option")

# Draw box border


def main(stdscr):
    stdscr.clear()
    ## Adding choices text
    position = 1
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlightText = curses.color_pair(1)
    normalText = curses.A_NORMAL
    for i in range( 1, max_row + 1 ):
        if row_num == 0:
            box.addstr( 1, 1, "There aren't strings", highlightText )
        else:
            if (i == position):
                box.addstr( i, 2, str( i ) + " - " + choices[ i - 1 ], highlightText )
            else:
                box.addstr( i, 2, str( i ) + " - " + choices[ i - 1 ], normalText )
            if i == row_num:
                break
    def draw_box(position, choices, row_num):
        for i in range( 1, max_row + 1 ):
            if row_num == 0:
                box.addstr( 1, 1, "There aren't strings", highlightText )
            else:
                if (i == position):
                    box.addstr( i, 2, str( i ) + " - " + choices[ i - 1 ], highlightText )
                else:
                    box.addstr( i, 2, str( i ) + " - " + choices[ i - 1 ], normalText )
                if i == row_num:
                    break
    stdscr.refresh()
    box.refresh()
    x = stdscr.getch()
    while x != 27: # 27 is ESC
        x = stdscr.getch()
        if x == curses.KEY_UP:
            if position >= 1:
                position = position - 1
                # Update the screen
            if position < 1:
                position = i
            draw_box(position, choices, row_num)
            stdscr.refresh()
            box.refresh()
        elif x == curses.KEY_DOWN:
            if position <= i:
                position = position + 1
                # Update the screen
            if position > i:
                position = 1
            draw_box(position, choices, row_num)
            stdscr.refresh()
            box.refresh()
        elif x == ord("1") or x == ord("2") or x == ord("3") or x == ord("4") or x == ord("5") or x == ord("6") or x == ord("7") or x == ord("8") or x == ord("9"):
            position = int(chr(x))
            draw_box(position, choices, row_num)
            stdscr.refresh()
            box.refresh()
        elif x == curses.KEY_ENTER or x in [10, 13]:
            stdscr.addstr( curses.COLS //2 , 0 , "You have chosen: " + str( position ) + " - " + choices[ position - 1 ] )
            stdscr.refresh()
            box.refresh()

            
        #Clear first line
        stdscr.addstr( 0, 0, " " * 80 )
        stdscr.addstr( 0, 0, "Choice: " + str( position) + " - " + choices[ position - 1 ] )
        stdscr.refresh()
        box.refresh()
    # Update the screen
    curses.endwin()

if __name__ == "__main__":
    try:
        os.system("cls" if os.name == "nt" else "clear")
        wrapper(main)
    except KeyboardInterrupt:
        print("\nProgram has been terminated!")
    finally:
        print("Goodbye!")

