num1=int(input("enter the num"))
num2=int(input("enthe the num"))
print("select the opreation")
print("1.add the num")
print("2.subtract the num")
print("3.Multiplication")
print("4.division")
choice=input("enter the choice")
if choice=="1":
    print("result",num1+num2)
elif choice=="2":
    print("result;",num1-num2)
elif choice=="3":
    print("result:",num1*num2)
elif choice=="4":
    print("result:",num1/num2)
else:
    print("invalid choice")
