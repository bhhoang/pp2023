import os

def input_info():
    stuID = input("Enter student ID: ")
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
                return -1
    else:
        return -1

def consecutive_input():
    n = int(input("Enter number of students: "))
    list_of_students = []
    for i in range(n):
        list_of_students.append(input_info())
    return list_of_students

def write_info(name, stuID, dob, delimiter):
    if(os.path.exists("./student.csv")):
        with open("./student.csv", "a") as f:
            f.write(f"{stuID}{delimiter}{name}{delimiter}{dob}\n")
    else:
        with open("./student.csv", "w") as f:
            f.write(f"Student ID{delimiter}Name{delimiter}Birthday\n")
            f.write(f"{stuID}{delimiter}{name}{delimiter}{dob}\n")

def disp(delimiter):
    with open("./student.csv", "r") as f:
        for line in f:
            print(line.replace(delimiter, "\t"))

def main():
    delimiter = ","
    choice = ["Input student's information", "Print student's information", "Set delimiter", "Enter with specify an amount of students" ,"Exit"]
    yn = "y"
    while(yn == "y"):
        for i in range(len(choice)):
            print(f"{i+1}. {choice[i]}")
        print("Please choose an option: ", end="")
        option = int(input())
        if(option == 1):
            name, stuID, dob = input_info()
            write_info(name, stuID, dob, delimiter)
        elif(option == 2):
            disp(delimiter)
        elif(option == 3):
            if(check_for_Delimiter() != -1):
                delimiter = check_for_Delimiter()
                print(f"The student file has already got delimiter which is {delimiter}")
            else:
                delimiter = input("Please input the delimiter (default is ,): ")
        elif(option == 4):
            list_of_students = consecutive_input()
            for i in range(len(list_of_students)):
                write_info(list_of_students[i][0], list_of_students[i][1], list_of_students[i][2], delimiter)

        elif(option == 5):
            yn = "n"
        else:
            print("Invalid option")

main()
