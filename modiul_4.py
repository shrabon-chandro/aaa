#Modiul=4

#class:-1
# OOP=Object-Oriented Programming Introduction

"""
class MyClass:
    x=12
    y=13
    z=15
    sum=x+y+z
oop1 = MyClass()
print(oop1.x)

oop2 = MyClass()
print(oop2.y)

oop3 = MyClass()
print(oop3.x)
"""
# class:-2
#OOP class variables, class methods

# class methods
"""
class MyClass:
    x=12
    y=13
    z=15

    def class_method(self,a,b,c):
        sum=self.x+self.y+self.z+a+b+c
        print(sum)
    def new_sum(self):
        self.class_method(2,3,5)

obj= MyClass()

obj.class_method(10,20,30)
obj.new_sum()
"""
#class variables
"""
class MyClass:
    x=12
    y=13
    z=15
    def class_attribute(self):
        return MyClass
obj = MyClass()
print(obj.x)
print(obj.y)
print(obj.z)
"""
# class:-3
# What is OOP Constructors Why How?

#Constructors Without Parameter
"""
class MyClass:
    def __init__(self):
        List="Hello world"
        print(List)

obj= MyClass()"""


# Constructors With Parameter
"""
class MyClass:
    x=10
    y=15


def __init__(self,a,b,c):
        sum=self.x+self.y+a+b+c
        print(sum)

obj= MyClass(2,22,2)
# Constructors obj == Constructors parenthisis
"""

#Instance Variables + Change Class Variable Using Constructor Params
"""
class MyClass:
    x=10#5
    y=15
    #z=100
    def __init__(self,zValue,xValue):
        self.z = zValue
        self.x = xValue
obj= MyClass(100,5)
print(obj.x)
print(obj.y)"""

#Instance Methods
"""
class MyClass:
    x=10 #5
    y=15
    #z=100
    def __init__(self,zValue,xValue):
        self.z = zValue
        self.x = xValue

    def addTwo(self):
        print(self.x + self.y + self.z)
obj= MyClass(100,5)
print(obj.x)
print(obj.z)
obj.addTwo()
"""
#class:-4
# OOP Static Properties

# static method
"""
class MyClass:
    x=10
    y=20
    @staticmethod
    def addTwo():
        print(MyClass.x + MyClass.y)

    @staticmethod
    def mul():
        print(MyClass.x * MyClass.y)
MyClass.addTwo()
MyClass.mul()

#or

obj = MyClass()
obj.addTwo()
obj.mul()
"""

# static value
"""
class MyClass:
    x=15
    y=20
    @staticmethod
    def mango():
        return MyClass

print(MyClass.x)
print(MyClass.y)

"""

#or
"""
obj = MyClass()
print(obj.x)
print(obj.y)
"""
# class:- 5
# What is OOP Inheritance(উত্তরাধিকার) Why How ?

# Single Inheritance(উত্তরাধিকার)
"""
class Father:  # parent class
    x=15
    y=25

    def add(self):
        print(self.x + self.y)
    def sub(self):
        print(self.x - self.y)
    def mul(self):
        print(self.x * self.y)

class son(Father):  # child class
    pass # কোনো কিছু না লিখলে pass লিখতে হয়

obj=son()
obj.add()
obj.sub()
obj.mul()
print(obj.x)
print(obj.y)
"""
# Multiple Inheritance
"""
class Father:  # parent class
    x=15
    y=25

    def add(self):
        print(self.x + self.y)
    def sub(self):
        print(self.x - self.y)

class Mother:  # parent class
    m=5
    n=50

    def div(self):
        print(self.m / self.n)
    def mul(self):
        print(self.m * self.n)

class son(Father,Mother):  # child class
    pass # কোনো কিছু না লিখলে pass লিখতে হয়

obj=son()
obj.add()
obj.sub()
obj.mul()
obj.div()
print(obj.x)
print(obj.y)
print(obj.m)
print(obj.n)
"""
# Multilevel Inheritance
"""
class Grandfather:  # parent class
    x=15
    y=25

    def add(self):
        print(self.x + self.y)
    def sub(self):
        print(self.x - self.y)
    def mul(self):
        print(self.x * self.y)
        
class Father(Grandfather):  # child class
    pass
class son(Father):  # child class
    pass # কোনো কিছু না লিখলে pass লিখতে হয়

obj=son()
obj.add()
obj.sub()
obj.mul()
print(obj.x)
print(obj.y)
"""
# class:- 6
# OOP Inheritance Constructor

# 1.When Parent class has, but the child class has not
"""
class Father:
    x=15
    y=25
    def __init__(self):
        print("Father Constructor")

class Son(Father):
    pass
obj = Son()
"""
# 2.When child class has, but the parent class has not
"""
class Father:
    x=15
    y=25


class Son(Father):
    def __init__(self):
        print("Son Constructor")
obj = Son()
obj = Father()
"""
# 3.When Parent and child both has contractor
"""
class Father:
    x=15
    y=25
    def __init__(self):
        print("Father Constructor")

class Son(Father):
    def __init__(self):
        print("Son Constructor")
obj = Son()
obj = Father()
"""
# 4.Accessing the Parent's Constructor
"""
class Father:
    x=15
    y=25
    def __init__(self):
        print("Father Constructor")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Constructor")
obj = Son()
"""
# class:- 7
# OOP Static Properties in Inheritance

#If Parent has static properties, child can access as it is like parent
"""
class Father:
    x=15
    y=25

    @staticmethod
    def addTwo():
        print(Father.x + Father.y)

class Son(Father):
    pass
Father.addTwo()
Son.addTwo()
"""
#If Child has static properties, Parent can't access as it is like child
"""
class Father:
    pass

class Son(Father):
    x = 15
    y = 25

    @staticmethod
    def addTwo():
        print(Son.x + Son.y)

Son.addTwo()
"""

# How child can access parents static and non-static propertie
"""
class Father:
    x=15
    y=20

    def addTwofather(self):
        print(self.x + self.y)

class Son(Father):
    def addTwoSon(self):
        print(self.x + self.y)
obj = Son()
obj.addTwoSon()

# OR OR OR

class Father:
    x=15
    y=20


    def addTwofather(self):
        return (self.x + self.y)

class Son(Father):
    def addTwoSon(self):
        sum = self.addTwofather()+100 ####
        print(sum)
obj = Son()
obj.addTwoSon()
"""

# class:- 8
# OOP Method Overriding

"""
class Father:
    x=15
    y=25
    def addTwo(self):
        print(self.x + self.y)

class Son(Father):
    def addTwo(self):
        print(self.x+5 + self.y)
obj = Son()
obj.addTwo()
print(obj.x)

"""

# class:- 9
# OOP Abstract Class & Methods
# How to create a abstract class

# Abstract class without enforcing any abstract method
"""
from abc import ABC,abstractmethod

class Bangladesh(ABC):
    def number0to11(self):
        pass
    def number0to16(self):
        for i in range(16):
            print(i)
class Dhaka(Bangladesh):
        pass

obj = Dhaka()
obj.number0to16()
"""
# Abstract class with enforcing one or more abstract method
"""
from abc import ABC,abstractmethod

class Bangladesh(ABC):
    @abstractmethod # বিমুর্ত বা ভুত
    def number0to11(self):
        pass
    @abstractmethod  # বিমুর্ত বা ভুত
    def number11to20(self):
        pass

    def number0to16(self):
        for i in range(16):
            print(i)
    def number16to31(self):
        for i in range(31):
            print(i)

class Dhaka(Bangladesh):
    def number0to11(self):
        pass
    def number11to20(self):
        pass

obj = Dhaka()
obj.number0to16()
obj.number16to31()
"""

# class:- 10
"""
class Father:
    x=15
    y=10
    def addtwo(self,a=0,b=0):
        print(self.x + self.y+a+b)
    def addtwo(self,m=0,n=0,o=0):
        print(self.x + self.y+m+n+o)
obj = Father()
obj.addtwo()
obj.addtwo(5,5)
obj.addtwo(2,2,2)
"""
# variable
"""
class Father:
    x=15
    y=10
    def addtwo(self,a=0,b=0):
        print(self.x + self.y+a+b)
    def addtwo(self,m=0,n=0,o=0):
        print(self.x + self.y+m+n+o)

    def variable(self,*a):
        print(a)

obj = Father()

obj.addtwo()
obj.addtwo(5,5)
obj.addtwo(2,2,2)

obj.variable(1)
obj.variable(1,2)
obj.variable(1,2,3)
obj.variable(1,2,3,4)
"""
# class:-11
# OOP Access Modifier

# Public Access modifiers
"""
1. Attributes and methods are public by default.
2. They can be accessed and modified both inside and outside the class
3. There are no restrictions on public attributes
4. (Inside Class) + ( Child Class ) + (Out Side of Class)
"""
"""
class CAR:
    Brand = "Toyota"

    def display(self):
        print(f"This is my car display : {self.Brand}")

obj = CAR()
obj.display()
print(obj.Brand)
"""
# Protected Access modifiers
"""
Protected Access modifiers

1. (Inside Class) + ( Child Class ) + (Out Side of Class (XX))
2. prefixed with a single underscore are protected.
"""
"""
class CAR:
    _br = "Bmw"
    _Brand = "Toyota"

    def display(self):
        print(f"This is my car display : {self._Brand}")
class Bike(CAR):
    def Displaylike(self):
        print(f"This is my car display : {self._Brand}")

obj = Bike()
obj.Displaylike()
print(obj._Brand)

"""

#Private Access modifiers
"""
Private Access modifiers

1. (Inside Class) + ( Child Class (XXX)) + (Out Side of Class (XXX))
2. prefixed with a single underscore are private.
"""
"""
class CAR:
    __Brand = "Toyota"

    def display(self):
        print(f"This is my car display : {self.__Brand}")
class Bike(CAR):
    def Displaylike(self):
        print(f"This is my car display : {self.__Brand}")

obj = CAR()
obj.display() 

#obj=Bike()
#obj.Displaylike() #(XXX)
# print(obj.__Brand)#(XXX)
"""


# class:- 12
# OOP Getter Setter In Python Private Properties

# Getter In Python Private Properties
"""
class COUMPUTER:
    __Brand = "acer"
    def coumputer(self):
        return self.__Brand

obj = COUMPUTER()
print(obj.coumputer()) ###
"""
#OR OR OR
#Getter:-
"""
class COUMPUTER:
    __Brand = "hp"
    @property
    def coumputer(self):
        return self.__Brand

obj = COUMPUTER()
print(obj.coumputer) #######
"""
"""
# setter:-

class COUMPUTER:

    __Brand = "hp"

    @property
    def coumputer(self):
        return self.__Brand

    @coumputer.setter
    def coumputer(self,value):
        self.__Brand=value


obj = COUMPUTER()
obj.coumputer="Doyel"

print(obj.coumputer)
"""
#class:- 13
#  OOP Encapsulation In Python
"""
class BANK_ACOUNT:

    __Balance = 0

    # Deposit
    def deposit_balance(self,amount):
        if amount>0:
            self.__Balance +=amount
            print("Deposit successfully")
        else:
            print("Invalid Balance")
    # Withdraw
    def withdraw_balance(self,amount):
        if amount>0 and amount<=self.__Balance:
            self.__Balance -=amount
            print("Withdraw successfully")
        else:
            print("Indufficient amount")
    # Check Balance
    def check_balance(self):
        return self.__Balance


obj = BANK_ACOUNT()
obj.deposit_balance(500)
print(obj.check_balance())
obj.withdraw_balance(50)
print(obj.check_balance())

# class:- 14
# OOP Polymorphism
"""
    .....
    ..
    ...
    ....
    ....
"""
