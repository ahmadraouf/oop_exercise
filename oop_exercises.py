class Employee:
    
    def __init__(self , employee_number, name, address, salary, job_title):
        self.employee_number = employee_number
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__job_title = job_title
        
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address
        
    def get_salary(self):
        return self.__salary
    
    def get_job_title(self):
        return self.__job_title
    
    def print_result_horizantal(self):
        print("Employee Information :""Employee Number = ",self.employee_number ,"Name = ", self.__name ,"Address = ", self.__address , "Salary = " , self.__salary , "Job title = ",self.__job_title)
      
    def print_result_vretical(self):
        print("Employee Information :","\nEmployee Number = ",self.employee_number ,"\nName = ", self.__name ,"\nAddress = ", self.__address , "\nSalary = " , self.__salary , "\nJob title = ",self.__job_title)
        
    def __del__(self):
        print(self.__name + " has been deleted")

first_employee = Employee(1,"Mohammad Khaled", "Amman,Jordan", 500, "Consultant")
second_employee = Employee(2,"Hala Rana", "Aqaba,Jordan", 750, "Manager")
first_employee.set_address("USA")
first_employee.print_result_horizantal()
first_employee.print_result_vretical()
print("First employee address :", first_employee.get_address())

del first_employee
del second_employee
