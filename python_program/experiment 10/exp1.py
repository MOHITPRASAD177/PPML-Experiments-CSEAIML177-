class Employee:
    def __init__(self, empid, name, basic_pay):
        self.empid = empid
        self.name = name
        self.basic_pay = basic_pay
        self.ta = 0
        self.da = 0
        self.gross_pay = 0.0
        print("employee",name,"id",empid)
    def calc(self):
        self.ta = 0.1 * self.basic_pay
        self.da = 0.4 * self.basic_pay
        self.gross_pay = self.basic_pay + self.ta + self.da
    
    def disp(self):
        print("\nemployee details")
        print("employee id:",self.empid)
        print("employee name:",self.name)
        print("basic pay:",self.basic_pay)
        print("ta:",self.ta)
        print("da:",self.da)
        print("gross pay:",self.gross_pay)
        
emp_id = int(input("enter employee id:"))
name = input("enter employee name:")
basic = float(input("enter basic pay:"))
obj = Employee(emp_id, name, basic)
obj.calc()
obj.disp()        