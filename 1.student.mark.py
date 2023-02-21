import os

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

# Single input student block
def input_info():
    courseId, courseName, stuID, courseMark = "","","",""
    stuID = input("Enter student ID: ")
    if checkDuplicate(stuID):
        choice = input("Duplicate student ID found! Do you want to continue?[y/n]")
        if choice.lower() == "y":
            name,dob = getName(stuID)
            courseId = input("Enter course ID: ")
            courseName = input("Enter course name: ")
            courseMark = input("Enter course mark: ")
            return stuID, name, dob, courseId, courseName, courseMark
        elif choice.lower() == "n":
            return None
    else:
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        courseId = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        courseMark = input("Enter course mark: ")
        return stuID, name, dob, courseId, courseName, courseMark

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
def consecutive_input(n:int):
    list_of_students = []
    for i in range(n):
        stuID,name, dob,courseId,courseName, courseMark = input_info()
        while(i > 0 and stuID == list_of_students[i-1][0]):
            print("WARN: Student ID already exists")
        list_of_students.append([stuID,name, dob,courseId,courseName, courseMark])
    return list_of_students

#Write to file
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
    if(os.path.exists("./student.csv")):
        name,dob = getName(stuID)
        print("+"+"-"*50+"+")
        print("| Student ID: " + stuID)
        print("| Name: " + name )
        print("| Date of Birth: " + dob)
        print("+"+"-"*50+"+")
        with open("./student.csv", "r") as f:
            for line in f:
                args = line.split(delimiter)
                if args[0] == stuID:
                    print("|")
                    print(f"+----Course Name: {args[4]}")
                    print("|\t|")
                    print(f"|\t+----Course ID: {args[3]}")
                    print("|\t|")
                    print(f"|\t+----Course Mark: {args[5]}", end="")
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
            stuID, name, dob, courseID,courseName, courseMark = input_info()
            write_info(name, stuID, dob,courseID,courseName,courseMark, delimiter)
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
            list_of_students = consecutive_input(amount)
            for i in range(len(list_of_students)):
                if(checkDuplicate(list_of_students[i][1]) == False):
                    write_info(list_of_students[i][0], list_of_students[i][1], list_of_students[i][2], list_of_students[i][3],list_of_students[i][4],list_of_students[i][5], delimiter)
                else:
                    print("Duplicate student ID!")
        elif(option == "5"):
            if os.path.exists("./student.csv"):
                os.remove("./student.csv")
                print("The file has been removed!")
            else:
                print("The file does not exist!")
        elif(option == "6"):
            stuID = input("Please input the student ID: ")
            inspectStudent(stuID, delimiter)
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
        print("Goodbye!")
