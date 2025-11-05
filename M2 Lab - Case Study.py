#Baker Hewitt
#M2 Lab - Case Study
#Determines which bracket, if any, a student is in based on GPA.

while True:
    last_name = input("Enter student's last name (Or 'ZZZ' to quit):")
    if last_name == "ZZZ":
        print("Program has ended.")
        break
    first_name = input("Enter student's first name:")
    gpa = float(input("Enter student's GPA:"))
    
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's list.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "has not made Honor Roll or the Dean's list.")
    
        
    
        
