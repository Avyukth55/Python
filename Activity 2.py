print("Enter a number")
num=int(input())
if num>=50:
    if num%2==0:
        print("Number is greater than 50, and is even")
    else:
        print("Number is greater than 50, and is odd")
else:
    print("Number is less than 50")