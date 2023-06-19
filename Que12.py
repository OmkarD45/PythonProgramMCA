'''
An organization has decided to provide salary hike to its employees 
based on their job level. Employees can be in job levels 3 , 4 or 5. 
Hike percentage based on job levels are given below:
Job level Hike Percentage (applicable on current salary)
3 15
4 7
5 5
In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a python program to 
find and display the new salary of an employee.(Note : You have to 
use Class , functions and exception handling concepts)
'''
class SalaryCalculator:
    def __init__(self, current_salary):
        self.current_salary = current_salary

    def calculate_new_salary(self, job_level):
        try:
            if job_level == 3:
                hike_percentage = 15
            elif job_level == 4:
                hike_percentage = 7
            elif job_level == 5:
                hike_percentage = 5
            else:
                hike_percentage = 0

            hike_amount = (hike_percentage / 100) * self.current_salary
            new_salary = self.current_salary + hike_amount

            return new_salary

        except Exception as e:
            print("Error:", str(e))
            return -1


# Take input from the user for current salary and job level
try:
    current_salary = float(input("Enter the current salary: "))
    job_level = int(input("Enter the job level (3, 4, or 5): "))

    # Create an instance of the SalaryCalculator class
    calculator = SalaryCalculator(current_salary)

    # Call the calculate_new_salary method to get the new salary
    new_salary = calculator.calculate_new_salary(job_level)

    if new_salary == -1:
        print("Invalid job level. Please enter a valid job level.")
    else:
        print("New salary: Rs", new_salary)

except ValueError:
    print("Invalid input. Please enter valid values.")
