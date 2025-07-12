# student_info=[]

# def main():
#     while True:
#         try:
#             student_info_part=[]
            
#             student_Id=int(input("Enter the Student Id: ")) 
#             student_Name=input("Enter the name of the Student: ").capitalize()
#             student_Course=input("Enter the course in which student admited: ").capitalize()
#             student_date_of_Birth=input("Enter date of birth in (yy/dd/mm): ")
#             student_Father_name=input("Enter the name of his Father:").capitalize()
#         except Exception as e:
#             print(f"Enter correct output if not then its give the error {e}")
        
#         student_info_part.append(student_Id)
#         student_info_part.append(student_Name)
#         student_info_part.append(student_Father_name)
#         student_info_part.append(student_date_of_Birth)
#         student_info_part.append(student_Course)
        
#         student_info.append(student_info_part)
#         print(student_info)
        
#         add_another=input("Do you want to enter one more student (yes/no) : ").lower()

#         if add_another == "no":
#             print("Thank you ")
#             break
        
        
        
        
# main()

# for info in student_info:
#     print(info)
    
    
    
    
    
# this is the another method 
def get_student_info():
    student_info = {}
    # Collecting student data
    try:
        student_info['student_Id'] = int(input("Enter the Student Id: "))
        student_info['student_Name'] = input("Enter the name of the Student: ").capitalize()
        student_info['student_Course'] = input("Enter the course in which student is admitted: ").capitalize()
        student_info['student_date_of_Birth'] = input("Enter date of birth in (yy/dd/mm): ")
        student_info['student_Father_name'] = input("Enter the name of his Father: ").capitalize()
        
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid data.")
        return None

    return student_info


def main():
    student_info_list = []  # List to store data for all students

    while True:
        student_info = get_student_info()
        
        if student_info:
            student_info_list.append(student_info)  # Add the student's data to the list
            print("\nStudent data entered successfully.")
        
        add_another = input("Do you want to enter one more student (yes/no): ").lower()
        if add_another == "no":
            print("Thank you for entering student data.")
            break

    print("\nAll students' information:")
    for student in student_info_list:
        print(student)


# Run the program
main()
