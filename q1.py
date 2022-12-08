num1=int(input())
num2=int(input())
num3=int(input())
if (num1>=num2) and (num1>=num3):
    m=num1
elif (num2>=num1) and (num2>=num3):
    m=num2
else:
    m=num3
print("m",m)
