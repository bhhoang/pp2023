import os

def input_info():
    stuID, name, dob = "", "", ""
    stuID = input("Enter student ID: ")
    if checkDuplicate(stuID):
        print("Duplicate student ID!")
        input_info()
        return stuID, name, dob
    else: None
    name = input("Enter student name: ")
    dob = input("Enter student's birthday: ")
    return stuID, name, dob

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

def checkDuplicate(stuID:str, delimiter:str = ","):
    if(os.path.exists("./student.csv") == False):
        return False
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            if args[0] == stuID:
                return True
    return False

def lookforLongest(delimiter:str = ","):
    longest = [0,0,0]
    with open("./student.csv", "r") as f:
        for line in f:
            args = line.split(delimiter)
            for i in range(3):
                if len(args[i]) > longest[i]:
                    longest[i] = len(args[i])
    return longest


def consecutive_input(n:int):
    list_of_students = []
    for i in range(n):
        stuID,name, dob = input_info()
        if i > 0 and stuID == list_of_students[i-1][0]:
            print("Duplicate student ID! Please re-enter!")
            consecutive_input(n-i)
        list_of_students.append([name, stuID, dob])
    return list_of_students


def write_info(name:str, stuID:str, dob:str, delimiter:str = ","):
    if(os.path.exists("./student.csv")):
        with open("./student.csv", "a") as f:
            ls = [stuID, name, dob]
            f.write(delimiter.join(ls) + "\n")
    else:
        print("File students.csv not found in current working directory, creating one...")
        with open("./student.csv", "w") as f:
            ls = ["Student ID", "Name", "Date of Birth"]
            f.write(delimiter.join(ls)+ "\n")
            ls = [stuID, name, dob]
            f.write(delimiter.join(ls) + "\n")

def disp(delimiter:str = ","):
    print("\n\n\n")
    if(os.path.exists("./student.csv")):
        longest = lookforLongest()
        with open("./student.csv", "r") as f:
            first_line = f.readline()
            args = first_line.split(delimiter)
            #remove the newline character
            args[2] = args[2][:-1]
            print("+ "+"-"*(longest[0]+longest[1]+longest[2]+18)+"+")
            print ("| " + args[0].ljust(longest[0]+4) + " | " + args[1].ljust(longest[1]+4) + " | " + args[2].ljust(longest[2]+4)+ "|")
            print ("+ " + "-"*(longest[0]+4) + " + " + "-"*(longest[1] + 4) + " + " + "-"*(longest[2]+4) + "+")
            for line in f:
                args = line.split(delimiter)
                args[2] = args[2][:-1]
                print ("| " + args[0].ljust(longest[0]+4) + " | " + args[1].ljust(longest[1]+4) + " | " + args[2].ljust(longest[2]+4)+ "|")
                print("+ "+"-"*(longest[0]+longest[1]+longest[2]+18)+"+")
    else:
        print("File students.csv not found in current working directory, creating one...")
        with open("./student.csv", "w") as f:
            ls = ["Student ID", "Name", "Date of Birth"]
            f.write(delimiter.join(ls)+ "\n")
    print("\n\n\n")
def main():
    delimiter = check_for_Delimiter() if check_for_Delimiter() else ","
    choice = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students","Remove data" ,"Exit"]
    yn = "y"
    while(yn == "y"):
        for i in range(len(choice)):
            print(f"{i+1}. {choice[i]}")
        print("Please choose an option: ", end="")
        option = input()
        if(option == "1"):
            stuID, name, dob = input_info()
            None if checkDuplicate(stuID) else write_info(name, stuID, dob, delimiter)
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
                    write_info(list_of_students[i][0], list_of_students[i][1], list_of_students[i][2], delimiter)
                else:
                    print("Duplicate student ID!")
        elif(option == "5"):
            if os.path.exists("./student.csv"):
                os.remove("./student.csv")
                print("The file has been removed!")
            else:
                print("The file does not exist!")
        elif(option == "6"):
            yn = "n"
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
