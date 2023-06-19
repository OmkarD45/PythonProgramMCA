'''
Write python code to display user defined exception for the condition” 
person having age less than 18 years i.e; voting age”.

'''
class UnderAgeException(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Person is under the voting age. Age: {age}")


def check_voting_age(age):
    if age < 18:
        raise UnderAgeException(age)
    else:
        print("Person is eligible to vote.")


# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_voting_age(user_age)
except UnderAgeException as e:
    print(e)
