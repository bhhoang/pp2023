import os

def input_info():
    stuID, name, dob = "", "", ""
    stuID = input("Enter student ID: ")
    if checkDuplicate(stuID): 
        print("Duplicate student ID!")
        return stuID, name, dob
    else: None
    name = input("Enter student name: ")
    dob = input("Enter student's birthday: ")
    return name, stuID, dob

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


def consecutive_input():
    n = int(input("Enter number of students: "))
    list_of_students = []
    for i in range(n):
        list_of_students.append(input_info())
    return list_of_students


def write_info(name, stuID, dob, delimiter):
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

def disp(delimiter):
    with open("./student.csv", "r") as f:
        for line in f:
            print(line.replace(delimiter, "\t"))

def main():
    global delimiter
    delimiter = "," if check_for_Delimiter() == False else check_for_Delimiter()
    choice = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students" ,"Exit"]
    yn = "y"
    while(yn == "y"):
        for i in range(len(choice)):
            print(f"{i+1}. {choice[i]}")
        print("Please choose an option: ", end="")
        option = int(input())
        if(option == 1):
            name, stuID, dob = input_info()
            None if checkDuplicate(stuID) else write_info(name, stuID, dob, delimiter)
        elif(option == 2):
            disp(delimiter)
        elif(option == 3):
            if(check_for_Delimiter()):
                delimiter = check_for_Delimiter()
                print(f"The student file has already got delimiter which is {delimiter}")
            else:
                delimiter = input("Please input the delimiter (default is ,): ")
        elif(option == 4):
            list_of_students = consecutive_input()
            for i in range(len(list_of_students)):
                if(checkDuplicate(list_of_students[i][1]) == False):
                    write_info(list_of_students[i][0], list_of_students[i][1], list_of_students[i][2], delimiter)
                else:
                    print("Duplicate student ID!")
        elif(option == 5):
            yn = "n"
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
