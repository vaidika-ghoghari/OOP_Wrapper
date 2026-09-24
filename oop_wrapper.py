#-----base class ------

class Employee:

    def __init__(self, emp_id ,name , age , __salary):
        self.emp_id = emp_id
        self.name = name
        self.age =age
        self.salary = salary

    def get_salary(self):
        return self.__salary

    def set _salary(self,salary):
        if self.__salary >= 0:
            self.__salary += salary
        else :
            print("Salary don't be in negative.")
            
    def get_emp_id(self):
        return self.emp_id

  #  def set_salary(self,salary):

    
