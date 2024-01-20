import os
def clear():
    os.system('cls')
def operation(number1,number2,oper):
    dict={"+":number1+number2,
          "-":number1-number2,
          "*":number1*number2,
          "/":number1/number2}
    for i in dict:
        if oper=="+":
            return dict["+"]
        if oper=="-":
            return dict["-"]
        if oper=="*":
            return dict["*"]
        if oper=="/":
            return dict["/"]

number1=int(input("What's the first number?"))
print("+")
print("-")
print("*")
print("/")
operator=input("Pick an operation?")
number2=int(input("What's the second Number?"))
number3=operation(number1,number2,operator)
print(f"{number1} {operator} {number2} = {number3}")
val=input(f"Type y to continue with the {number3},or type n to start a new calculation?")
number5=number3
while val!="n":
    entry=input("Enter X to end else to continue")
    if entry=="X":
        break
    else:       
      number4=int(input("Enter the new number: "))
      operat=input("Pick a opeartion?")
      number5=operation(number5,number4,operat)
      print(number5)
clear()