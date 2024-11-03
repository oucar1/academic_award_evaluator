# Author: Ozgur Ucar
# File Name: academic_award_evaluator.py
"""Description: This app accepts a student's last name, first name, and GPA, 
then determines if the student qualifies for the Dean's List or Honor Roll."""

if __name__ == "__main__":
    while True:
        # Get student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        
        # Quit if 'ZZZ' is entered
        if last_name == 'ZZZ':
            print("Exiting the program.")
            break
        
        # Get student's first name and GPA
        first_name = input("Enter the student's first name: ")
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a numeric value.")
            continue
        
        # Determine if the student qualifies for Dean's List or Honor Roll
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")