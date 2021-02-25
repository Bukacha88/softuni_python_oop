class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.salary = salary
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())