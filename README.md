# Employee Management System

A simple **Python-based Employee Management System** developed to demonstrate the practical implementation of **Object-Oriented Programming (OOP)** concepts.

The system allows users to create Employees, Managers, and Developers, store their objects in a list, and display their details through a menu-driven program.

## Features

* Create an Employee
* Create a Manager
* Create a Developer
* Store employee objects in a list
* Display Employee details
* Display Manager details
* Display Developer details
* Salary validation
* Getter and Setter methods
* Menu-driven interface
* Inheritance
* Method overriding
* Constructor and Destructor

## OOP Concepts Used

### 1. Class and Object

The project uses three classes:

* `Employee`
* `Manager`
* `Developer`

Objects are created from these classes according to the user's choice.

### 2. Encapsulation

The salary of an employee is kept private using double underscores:

```python
self.__salary = salary
```

Getter and setter methods are used to access and modify the salary.

```python
def set_salary(self, salary):
    if salary >= 0:
        self.__salary = salary

def get_salary(self):
    return self.__salary
```

This helps protect the salary data from direct access.

### 3. Inheritance

`Manager` and `Developer` inherit properties and methods from the `Employee` class.

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

This allows the derived classes to reuse the functionality of the base class.

### 4. Method Overriding

The `display()` method of the `Employee` class is overridden in both `Manager` and `Developer`.

```python
def display(self):
    super().display()
```

Each derived class adds its own specific information while also using the display method of the parent class.

### 5. Constructor

The `__init__()` method is used to initialize object data such as:

* Name
* Age
* Employee ID
* Salary
* Department
* Programming Language

### 6. Destructor

The `__del__()` method is used as a destructor.

```python
def __del__(self):
    print("Employee deleted successfully.")
```

It displays a message when an employee object is deleted.

### 7. List of Objects

All created Employee, Manager, and Developer objects are stored in a single list.

```python
employees = []
```

Objects are added to the list using:

```python
employees.append(employee)
employees.append(manager)
employees.append(developer)
```

The program then loops through the list to display the required type of employee.

## Project Structure

```text
Employee Management System
│
└── oop_wrapper.py
```

## Menu Options

```text
===== Employee Management System =====

Choose an operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
```

### Create an Employee

The user enters:

* Name
* Age

The Employee object is then created and stored in the `employees` list.

### Create a Manager

The user enters:

* Employee ID
* Name
* Age
* Salary
* Department

The Manager object is created and stored in the list.

### Create a Developer

The user enters:

* Employee ID
* Name
* Age
* Salary
* Programming Language

The Developer object is created and stored in the list.

### Show Details

The user can select:

```text
1. Employee Details
2. Manager Details
3. Developer Details
```

The program searches through the `employees` list and displays the selected type of employee.

## Example Output

```text
===== Employee Management System =====

Choose an operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit

Enter your choice: 2

=== ADD Manager ===

Enter Employee ID: 101
Enter Name: Rahul
Enter Age: 30
Enter Salary: 50000
Enter Department: HR

Manager created with name: Rahul, ID: 101, Age: 30,
Salary: 50000.0, Department: HR

--- Manager created successfully. ---
```

When Manager Details are selected:

```text
--- Display Managers ---

Name: Rahul
Age: 30
Employee ID (Manager): 101
Salary: 50000.0
Department: HR
```

## Salary Validation

The project prevents negative salary values.

```python
if salary >= 0:
    self.__salary = salary
else:
    print("Salary should not be negative.")
```

## Technologies Used

* **Python**
* **Object-Oriented Programming**
* **Python Lists**

## Requirements

* Python 3.x
* Any Python IDE such as:

  * VS Code
  * IDLE
  * PyCharm

No external libraries are required.

## How to Run

1. Install Python 3.x.
2. Download or clone the project.
3. Open `oop_wrapper.py` in your Python IDE.
4. Run the program.
5. Select an option from the menu.
6. Enter the required information.

You can also run it from the terminal:

```bash
python oop_wrapper.py
```

## Abstraction

Abstraction is **not implemented** in this project.

The project does not contain an abstract class or abstract method because abstraction was not required for this implementation.

## Method Overloading

Traditional method overloading is **not implemented** in this project.

Python does not support traditional method overloading like some other programming languages. The project focuses on other OOP concepts such as inheritance, encapsulation, and method overriding.

## Learning Outcomes

Through this project, I learned how to implement:

* Classes and Objects
* Constructors
* Destructors
* Encapsulation
* Private attributes
* Getter and Setter methods
* Inheritance
* Method Overriding
* Lists of Objects
* Menu-driven programs
* Basic data validation

## Future Improvements

The project can be extended in the future by adding:

* Update employee details
* Delete employee records
* Search employee by ID
* Automatic Employee ID generation
* Store data permanently using files
* Add a graphical user interface
* Add more employee roles

  
## 🎥 Project Explanation

I have also made an explanation video where I explain how this project works and the Python concepts used in it.

👉 **Watch the Project Explanation Video :** (https://drive.google.com/file/d/1Nx-D6Zs60MA53vqXK_7faDkAQudvNts5/view?usp=sharing)


##  📫 Connect With Me
If you would like to connect with me or see more of my projects:

- 💻 **Email:** [Vaidika_ghoghari](ghogharivaidika@gmail.com)
- 💼 **LinkedIn:** [LinkedIN]( www.linkedin.com/in/vaidika-ghoghari-2196a534a)


## Author

**Vaidika Ghoghari**

This project was created as part of an **Object-Oriented Programming practical project** to understand and demonstrate the use of OOP concepts in Python.

actical project** to understand and demonstrate the use of OOP concepts in Python.

