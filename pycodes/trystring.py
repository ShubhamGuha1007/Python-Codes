# Python String Programs

# 1. Calculate the length of the String.
# char=str(input("Enter the String ??"))
# print("The length of the string is ",len(char))


# 2. Count the no. of frequency of a given String.
# char=str(input("Enter the String ??"))
# print("{",end="")
# empty_char=""
# for i in char:
#     if i not in empty_char:
#         empty_char+=i
# for i in empty_char:
#     print(i," = ",char.count(i),",",end="")
# print("}")


#3. Fetch first and last two character of a String.
# char=str(input("Enter the String ??"))
# print(char[0:2]+char[-2:])


#4. All occurence of the first character replaced by $.
# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#   return str1
# print(change_char('restart'))


#5. Swap two String by space.
# def space(x,y):
#     return y+" "+x
# str1=str(input("Enter the first string ??"))
# str2=str(input("Enter the second string ??"))
# print(space(str1,str2))


# 6.add ing in the end of the string , if its there then add ly in the end of that string.
# str1=str(input("Enter the string ??"))
# temp_str=""
# if str1[-3:]!="ing":
#     temp_str+=str1+"ing"
# elif str1[-3:]=="ing":
#     temp_str+=str1+"ly"
# else:
#     temp_str=str1
# print(temp_str)


# 7.Return the length of the longest string.

# def long(x):
#     list1=[]
#     y=x.split()
#     length=0
#     for i in y:
#         store=len(i)
#         list1.append(store)
#     return str(max(list1))
# str1=str(input("Enter a String ??"))
# print(long(str1))


# 8. Remove the nth index of a String.
# def ret(x,y):
#     temp=x
#     return temp.replace(x[y],"")
# str1=str(input("Enter the String ??"))
# index=eval(input("Enter the nth value u want to eradicate from a string ??"))
# print(ret(str1,index))



# 9. Write a Program where first and last character is exchanged.
# def exc(word):
#     return word[-1]+word[1:-1]+word[0]
# word=str(input("Enter the String ??"))
# print(exc(word))



# 10.Write a Python program to remove the odd index from a given string.
# def odd(x):
#     new=""
#     for i in range(len(x)):
#         if i%2==0:
#             new+=x[i]
#     return new
# word=str(input("Enter the String"))
# print(odd(word))


# 11.Program to find the occuerences of each word in a sentences.
# def sent(x):
#     list=[]
#     for i in x.split():
#         if i not in list:
#             list.append(i)
#     for i in list:
#         print(i," = ",x.count(i))
#
# sen=str(input("Enter the string ??"))
# sent(sen)



# 12. Reverse a String.
# def rev(x):
#     return x[::-1]
#
# str1=str(input("Enter the string ??"))
# print(rev(str1))



# 13.Sort a String
# str1=str(input("Enter a String ??"))
# str2=str1.split()
# str3=sorted(str2)
# str4=" ".join(str3)
# print(str4)


# 14.Use startswith/endswith.
# def prog(x,y):
#     if x.endswith(y):
#         return True
#     else:
#         return False
# word=str(input("Enter the String ??"))
# sub=str(input("Enteer the word u looking on a given string ??"))
# print(prog(word,sub))



# 15.Take a String convert upper to lower and vice-versa.
# def conver(x):
#     text=""
#     for i in x:
#         if i.isupper():
#             text+=i.lower()
#         else:
#             text+=i.upper()
#     return text
# str1=str(input("Enter the String ??"))
# print(conver(str1))


# 16. Count the occurrences of a sub string.
# def occ(x,y):
#     for i in x.split():
#         if i==y:
#             return x.count(y)
#         else:
#             return "Get Lost"
#
# str1=str(input("Enter a String ??"))
# sub=str(input("Enter the substring ??"))
# print(occ(str1,sub))





# No. of Words and characters present on a string.
# string1=str(input("Enter the string ??"))
# letters=0;num=0
# for i in string1:
#     if i==" ":
#         pass
#     elif i.isdigit():
#         num+=1
#     else:
#         letters+=1
# print("The no. of letters present on the string is ",letters)
# print("The no. of words present on the string is ",len(string1.split()))
# print("The no. of numbers present on the the string is ",num)




# Anagram or Not
# str1=str(input("Enter a string ??"))
# str2=str(input("Enter a string ??"))
# str1=str1.upper()
# str2=str2.upper()
# str1=sorted(str1)
# str2=sorted(str2)
# if str1==str2:
#     print("Its an Anagram")
# else:
#     print("Its not an Anagram")




# Write a program to get 4 copies of last two character of a python.
# str1=str(input("Enter the String ??"))
# if(len(str1)<=2):
#     print(str1)
# else:
#     print(str1[-2:]*4)


# Write a Program to print first three letter of a string.
# str1=str(input("Enter the String ??"))
# if(len(str1)<=3):
#     print(str1)
# else:
#     print(str1[0:3])



# Remove odd and even elemets from a string.
# str1=str(input("Enter a String ??"))
# length=len(str1)
# odd="";even=""
# for i in range(length):
#     if i%2==0:
#         even+=str1[i]
#     else:
#         odd+=str1[i]
# print("The even string - ",even)
# print("The odd string - ",odd)



# letter=str(input("Enter a letter ??"))
# print("The AsCII value of the letter is ",ord(letter))
# print("The character of the integer value is ",chr(ord(letter)))
