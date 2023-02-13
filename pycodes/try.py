# 1.print program
# print("Hello World")


# 2.Sum of two numbers
# num1=eval(input("Enter the first number ??"))
# num2=eval(input("Enter the second number ??"))
# sum=num1+num2
# print("The sum of two number is ",sum)


# 3.Calculator
# num1=eval(input("Enter the first number ??"))
# num2=eval(input("Enter the second number ??"))
# print("****Choose the following operation****")
# print(" + = Addition")
# print(" - = Subtraction")
# print(" * = Multiplication")
# print(" / = Division")
# print(" % = Remainder")
# operation=str(input("Enter : "))
# if operation == "+":
#     op=num1+num2
# elif operation == "-":
#     op=num1-num2
# elif operation == "*":
#     op=num1*num2
# elif operation == "/":
#     op=num1/num2
# elif operation == "%":
#     op=num1%num2
# else:
#     op="Invalid"
# print("The following result is ",round(op))


#4. Palindorme Number
# num=eval(input("Enter the following number ??"))
# temp=num
# rev=0
# while(temp>0):
#     lastdigit=temp%10
#     rev=rev*10+lastdigit
#     temp//=10
# print("The reversed number is ",rev)
# if(rev==num):
#     print("Its a palindrome number")
# else:
#     print("Its not a palindrome number")



#5. Factorial
# num=eval(input("Enter the number ??"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print("The factorial of the following number is ",fact)


#6. Prime Number using function
# def prime(x):
#     flag=0
#     for i in range(2,num//2+1):
#         if(x%i==0):
#             flag=1
#             break
#     if flag==0 and x>=2:
#         print("Its a prime Number")
#     else:
#         print("Its not a prime Number")
# num=eval(input("Enter the following number ??"))
# prime(num)



#7. Table of a number
# num=eval(input("Enteer the number ??"))
# for i in range(1,11):
#     print(num," * ",i," = ",num*i)



#8. Armstrong Number
# num=eval(input("Enter the number ??"))
# temp=num;arm=0
# while(temp>0):
#     lastdigit=temp%10
#     arm=arm+(lastdigit**3)
#     temp//=10
# if(num==arm):
#     print("Its an Armstrong number")
# else:
#     print("Its not an Armstrong number")



#9. Leap Year
# num=eval(input("Enter the year ??"))
# if((num%400==0)or(num%4==0)and(num%100!=0)):
#     print("Its a leap Year")
# else:
#     print("Its not a leap Year")



#10. Fibonacci Series using function
# def fibo(num):
#     num1=0;num2=1;sum=0
#     print(num1)
#     print(num2)
#     for i in range(3,num+1):
#         sum=num1+num2
#         print(sum)
#         num1=num2
#         num2=sum
# ran=eval(input("Enter the range ??"))
# fibo(ran)




# Write a program to print the following intergers along with *(multiples of len of integers)
# def numbo(x):
#     length=len(str(x))
#     return str(x)+("*"*length)
#
# num=eval(input("Enter the number ??"))
# print(numbo(num))




# GCD
# def gcd(x,y):
#     minimum=min(x,y)
#     for i in reversed(range(1,minimum+1)):
#         if((x%i==0) and (y%i==0)):
#             return "The gcd of both the numbers is ",i
# num1=eval(input("Enter the first number ??"))
# num2=eval(input("Enter the second number ??"))
# print(gcd(num1,num2))


# LCM
# def lcm(x,y):
#     maximum=max(x,y)
#     flag=0
#     while True:
#         if((maximum%x==0)and(maximum%y==0)):
#             return "The gcd of both the numbers is ",maximum
#         else:
#             maximum+=1
# num1=eval(input("Enter the first number ??"))
# num2=eval(input("Enter the second number ??"))
# print(lcm(num1,num2))




# Range of Non Prime Numbers
# ran=eval(input("Enter the last number ??"))
# num=eval(input("Enter the numbers ??"))
# for z in range(0,ran+1):
#     for i in range(2,z):
#         if(z%i==0):
#             print(z,end=" ")
#             break




# Factorial using recursion
# def fact(x):
#     if x<=1:
#         return 1
#     else:
#         return x*fact(x-1)
#
# num=eval(input("Enter the number ??"))
# print(fact(num))


# Fibonacci Using recursion
# def fibo(x):
#     if x <= 1:
#         return x
#     else:
#         return (fibo(x-1) + fibo(x-2))
# num = eval(input("Enter the range ??"))
# if num <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(num):
#        print(fibo(i))




# Remove duplicate number from a given number.
# num=eval(input("Enter the Number ??"))
# snum=str(num)
# snum2=""
# for i in snum:
#     if i not in snum2:
#         snum2+=i
#     else:
#         snum.replace(i,"")
# print(snum2)



# Perfect Numbers from 1 to 100:
# for i in range(1,100+1):
#     factors=0
#     for z in range(1,i):
#         if i%z==0:
#             factors+=z
#     if factors==i:
#         print(factors)



# Print Co prime Numbers 1 to 100:
# count=0
# for i in range(2,10+1):
#     for j in range(i+1,10+1):
#        if j%i==1:
#            print(i,j)
