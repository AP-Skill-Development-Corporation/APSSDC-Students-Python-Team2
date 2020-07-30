class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display1(self):
        print("name:",self.name)
        print("age:",self.age)
class B(A):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display2(self):
        super().display1()
        print("rollno:",self.rollno)
class C(B):
    def __init__(self,name,age,rollno,branch):
        super().__init__(name,age,rollno)
        self.branch=branch
    def display3(self):
        super().display2()
        print("branch:",self.branch)
        