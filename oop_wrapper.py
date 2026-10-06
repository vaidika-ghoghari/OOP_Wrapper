#-----base class ------

class Employee:

    def __init__(self,name , age,emp_id = 0  , salary = 0):
        self.emp_id = emp_id
        self.name = name
        self.age =age
        self.__salary = salary

    
    def set_salary(self,salary):
        if salary >= 0:
            self.__salary = salary
        else :
            print("Salary should not be negative.")

    def get_salary(self):
            return self.__salary
    

    def set_emp_id(self,emp_id):
            self.emp_id = emp_id

    def get_emp_id(self):
        return self.emp_id

    

    def display(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")

    #destructor method
    def __del__(self):
            print("Employee deleted successfully.")

#---derived class: manager first---
class Manager(Employee):

    def __init__(self, name ,  age ,emp_id, salary, department):
        super().__init__(name ,  age ,emp_id, salary)
        self.department = department

    # override a display method 
    def display(self):         
        super().display()
        print(f"Employee ID : {self.get_emp_id()}")
        print(f"Salary: {self.get_salary()}")
        print(f"Department: {self.department}")

#---derived class: developer ---
class Developer(Employee):

    def __init__(self, name ,  age ,emp_id, salary, programming_language):
        super().__init__(name ,  age ,emp_id, salary)
        self.programming_language = programming_language

    # override a display method 
    def display(self):         
        super().display()
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Salary: {self.get_salary()}")
        print(f"Programming Language: {self.programming_language}")

employees = []
while True:

    print("\n===== Employee Management System =====")
    print("\nChoose an operation:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n=== ADD Employee ===")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        
        employee = Employee(name, age)
        employees.append(employee)
        
        print(f"\nEmployee created with name: {employee.name} , Age: {employee.age} ")
        print("\n--- Employee created successfully. ---")
        print("-"*50)

    elif choice == 2:
        print("\n=== ADD Manager ===")
        
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        
        manager = Manager(name, age, emp_id, salary, department)
        
        if issubclass(type(manager), Employee):
            employees.append(manager)
        
        print(f"\nManager created with name: {manager.name} , ID: {manager.emp_id} , Age: {manager.age} , Salary: {manager.get_salary()} , Department: {manager.department}")
        print("\n--- Manager created successfully. ---")
        print("-"*50)

    elif choice == 3:
        print("\n=== ADD Developer ===")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        programming_language = input("Enter Programming Language: ")
        
        developer = Developer(name, age, emp_id, salary, programming_language)
        
        if issubclass(type(manager), Employee):
            employees.append(developer)
        
        print(f"\nDeveloper created with name: {developer.name} , ID: {developer.emp_id} , Age: {developer.age} , Salary: {developer.get_salary()} , Programming Language: {developer.programming_language}")
        print("\n--- Developer created successfully. ---")
        print("-"*50)

    elif choice == 4:
        print("\nChoose Details to Show:")
        print("1. Employee Details")
        print("2. Manager Details")
        print("3. Developer Details")

        ch=int(input("Enter your choice: "))

        if ch == 1:
            print("\n--- Display Employees ---")
            for i in employees:
                if type(i) == Employee:
                    i.display()
                    
            print("-"*50)

        elif ch == 2:
            print("\n--- Display Mangers --- ")
            for i in employees:
                if type(i) == Manager:
                    i.display()
                    
            print("-"*50)
                  
        elif ch == 3:
            print("\n--- Display Developers ---")
            for i in employees:
                if type(i) == Developer:
                    i.display()
                    
            print("-"*50)
    
    elif choice == 5:
        print("\nExiting the system. All resources have been freed.")
        break

    else:
        print("\nInvalid choice. Enter a number between 1 and 5.")
