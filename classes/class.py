# method in class
class Method:
    # def __init__(self, emp_company_name):
    #     self.emp_company_name=emp_company_name
    # def Emp_data(self, emp_name, emp_id)  :
    #     self.emp_name = emp_name
    #     self.emp_id = emp_id

    # reference=Method


    class Student:
        def __init__(self, m1,m2, m3):
            self.m1=m1
            self.m2=m2
            self.m3=m3
        def avg(self):
            return (self.m1+self.m2+self.m3)/3
    # Average= Student()
    print(Student(10,30,20).avg())