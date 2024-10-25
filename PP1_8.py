'''
    Lesson: Boolean Logic
    Author: Karcihan Satheskishan
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''
def q1():
  bool1=True
  bool2=False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  num=int(input("Enter an integer: "))
  bool1=(num != 0)
  print(bool1)

def q3():
  num=float(input("Enter a number: "))
  bool1=(num >= 0 and num <= 10)
  print(bool1)

def q4():
  food=input("Input food: ")
  drink=input("Input drink: ")
  bool1=not(food == "pizza" and drink == "pop")
  print(bool1)

def q5():
  num=int(input("Enter an integer: "))
  bool1=(num%2==0)
  print(f"The integer {num} is {bool1}")

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''