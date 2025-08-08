#25 dtrd=["shan","sundar","sumit","ut","jag","vikas"]
# print(type(dtrd))
# list1 = dtrd[1,4]
# # print(list1)
# str1="sumitsolanke"
# if "itsol" in str1:
#     print("sumit does well")
# else:
#     print("suraj is fraud")
# for items in dtrd:
#     if "sunder" is there:
#         print("he is the one")
# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)
# colors = ["voilet", "indigo", "blue"]
# sem = colors.append("green")
# print(sem)
# # add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# rainbow.extend(colors)
# print(rainbow)
# def sumit(*a):
#     avg=sum(a)/len(a)
#     print(avg)
# sumit(91,99,95,93,91)
# def name (lname,fname="ajay",mname="vilas"):
#     print("Hello,", fname, mname, lname)
# name(lname="yande")
# str = ["sham","vikas","lal","haribol"]
# if "sham" in str:
#     print("He was present")/
# number=[7,5,3,1,9,4,6,2,3,0,8]
# number.reverse()
# number.sort()
# print(number)
# if 8 in number:
#         print("fulfilled")
# number.sort(reverse=number)
# print(number)
# print(number.index(3))
# print(number.count(3))
# newlist=number.copy()
# print(newlist)
# number.append(454)
# print(number)
# num=tuple(number)
# print(num)
# sumit=num.index(9)
# print(sumit)
# print(num[8])
# number=(1,8,9,7,2,88,15,46,92,28)
# print(type(number))
# print(number.find(9))
# Hours=float(input("enter the time in (HH.MM):"))
# def f(n):
#     '''create a f series'''
#     if(n==0):
#         return 0
#     elif(n==1 or n==2):
#         return 1
#     else:
#         return (f(n-1) + f(n-2))
# print(f(16)) if(Hours>=0 and Hours<12):
#     print("Good Morning Sir.")
# elif(Hours>=12 and Hours<17):
#     print("Good Afternoon Sir.")
# elif(Hours>=17 and Hours<24):
#     print("Good Night Sir.")
# else:
#     print("Nikal, BSDK")

# def factorial(num): 
#     if (num == 1 or num == 0):
#         print(1)
#     else:
#         print(f"{num} * {factorial(num - 1)}") 
# factorial(5)

# sert={}
# print(type(sert))

# sert=set()
# print(type(sert))

# info={"car",19, False ,5.9,19}
# for i in info:
#     print(i)


# num = {1,2,3,5,6,8}
# num1 = (7,0,5,8,9,4)
# num.update(num1)
# print(num)

# try:
#     num = int(input("Enter an integer index of value: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")

# # Kon Banega Carorepati(KBC)
# KBC="""'Hii, Everyone
# Welcome to the Beauty Full World of KBC.
# Here user will be asked some questions and they can earn Dhan Rashi.
# Are you ready??"""

# print(KBC)

# # First Question!!
# print("\nTHe First question will be shown on your computer Screen")
# print("Q.1 Which of the the following is a fruit?")
# fruit=["1. carrot","2. apple","3. potato","4. spinach"]
# for i in fruit:
#     print(i)

# ans1 = input("Enter your answer (1/2/3/4 or answer): ")
# an1=ans1.lower()
# if (an1=="apple" or "2"):
#         print("Sahi Javab!!!")
#         print("You won the dhan rashi of 500","\n&You are eligible for the next question.")
#         cash1 = 500
# else:
#         print("Sorry you lost.")
#         print("Going to next without winning anything")
#         cash1 = 0


# # Second Question!!
# print("\nQ.2) How many hours are there in a day?")
# Hrs=["1) 12","2) 24","3) 48","4) 60"]
# for j in Hrs:
#     print(j)
# ans2 = input("Enter your answer (1/2/3/4 or answer): ")
# if(ans2=="24" or "2"):
#         print("Sahi Javab!!!")
#         print("You won the dhan rashi of 1000","\n&You are eligible for the next question.")
#         cash2=1000
# else:
#         print("Sorry you lost.")
#         print("Going to next without winning anything")
#         cash2=0

# # Third Question!!

# print("\nQ.3) What do we use to write on Blackboard?")
# Bboard=["1.pen","2.chalk","3.pencil","4.marker"]
# for k in Bboard:
#     print(k)
# ans3=input("Enter your answer (1/2/3/4 or answer): ")
# an3=ans3.lower()
# if(an3=="chalk" or "2"):
#         print("Sahi Javab!!!")
#         print("You won the dhan rashi of 2000","\n&You are eligible for the next question.")
#         cash3=2000
# else:
#         print("Sorry you lost.")
#         print("Going to next without winning anything")
#         cash3=0

# # Fourth Question 
# print("\nQ.4) What is the capital of Bangladesh?")
# capital=["lahor","kabul","dhaka","khulana"]
# for l in capital:
#     print(l)
# ans4=input("Enter your answer (1/2/3/4 or answer): ")
# an4=ans4.lower()
# if(an4=="dhaka" or "3"):
#         print("Sahi Javab!!!")
#         print("You won the dhan rashi of 5000",)
#         cash4=5000
# else:
#         print("Sorry you lost.")
#         cash4=0
# print("\nNow the questions are over.")
# print("Gonna announce the prize money.")
# money= cash1 + cash2 + cash3 + cash4
# print(f"The Laxmi you won is: ${money}")
# print("CONGRAGULATION!!!!")


# a = int(input("Enter the value between 5 & 9 :"))
# if (a<5 or a>9):
#         raise ValueError("Value should be in between 5 & 9")
# elif(a = "quit"):


# Convert normal english into code language
# a = [input("Enter the English sentence you want to convert to secret code: ")]
# a.split(" ")
# for i in a:
#         if(a.len() < 3):
# print(a.reverse())

# marks = [12,24,85,99,45,26]
# for mark in marks:
#         print(mark)
#         if()


import sumit
# print(dir(sumit))
# result = sumit.AddCode()
# print(result)
# AddCode()
result = sumit.AddCode(2,3)
print(result)