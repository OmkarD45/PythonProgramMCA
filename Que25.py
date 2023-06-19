'''
Q.25 Create a class employee with attribute name and base_pay method
get_pay() which shouldr eturn base_pay.Class SalesEmployee with attribute
name, base_pay, Sales_incentives inherit employee class over-rides
get_pay() and return addition of base_pay and sales_incentive
'''


class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        super().__init__(name, base_pay)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive


emp = Employee("John Doe", 5000)
print(emp.get_pay())


sales_emp = SalesEmployee("Jane Smith", 4000, 1000)
print(sales_emp.get_pay())
