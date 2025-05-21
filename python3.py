# import random

# #1 Temperature Converter
# def temp(val, a):
#     result = 0
#     if a == 'c':
#         result = (val * 9 / 5) + 32
#         print(str(result) + 'F')
#     elif a== 'f':
#         result = (val - 32) * 5 / 9
#         print(str(result) + 'C')

# temp(60, 'c')
# temp(45, 'f')

# #2 Find numbers divisible by both 5 and 7
# for n in range(1500, 2701):
#     if n % 7 == 0 and n % 5 == 0:
#         print(n)

# #3 Number Guess
# num = random.randint(1, 9)
# while True:
#     a = int(input("Guess a number between 1 and 9: "))
#     if a == num:
#         print("Well guessed!")
#         break
#     else:
#         print("You are Wrong!")

#4 Pattern printing
        # n = 5
        # s = 1
        # flag= False
        # for r in range(0, 2 * n):
        #     for _ in range(0, s):
        #         print("*", end="")
        #     print("")
        #     if s < n and not flag:
        #         s += 1
        #     elif s == n and not flag:
        #         flag = True
        #         s -= 1
        #     else:
        #         s -= 1

# #5 Reverse string
# w = input("Enter a word: ")
# print(w[::-1])

# #6 Count even and odd
# lst = [1, 3, 12, 14, 35, 24]
# even = 0
# odd = 0
# for x in lst:
#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:", even, "Odd:", odd)

# #7 Show type of each item
# data = [6387, 5.55, 4+6j, True, "Hello there", (5, 5), [6, 7], {"a": 6, "b": 5}]
# for x in data:
#     print(x, type(x))

# # #8 Skip certain numbers
# for x in range(7):
#     if x == 3 or x == 6:
#         continue
#     print(x, end=" ")

# #9 Fibonacci until >50
# a = 0
# b = 1
# while True:
#     print(a)
#     a = b
#     b=a + b
#     if b > 50:
#         break

# #10 2D list value assign
row=3
col=4
array_2d= [[0 for j in range(col)] for i in range(row)]
for i in range(row):
  for j in range(col):
   array_2d[i][j]= i*j
  print("")
for i in range(row):
  for j in range(col):
   print(array_2d[i][j],end="")
  print("")


# # 11 
# lines = []
# while True:
#     line = input("Enter a line (blank to stop): ")
#     if not line:
#         break
#     lines.append(line.lower())

# for l in lines:
#     print(l)



# #12
# data = input("Enter binary numbers separated by commas: ")
# binaries = data.split(',')
# for b in binaries:
#     deci = int(b, 2)
#     if deci % 5 == 0:
#         print(b)

# text = input("Enter a string: ")
# # 13
# letters = 0
# digits = 0

# for ch in text:
#     if ch.isalpha():
#         letters += 1
#     elif ch.isdigit():
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)


# #14 password validation 

# def validate_password(password):
#     has_lower = False
#     has_upper = False
#     has_digit = False
#     has_special = False
#     special_chars = "$#@"

#     if len(password) < 6 or len(password) > 16:
#         return False

#     for char in password:
#         if char.islower():
#             has_lower = True
#         elif char.isupper():
#             has_upper = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_chars:
#             has_special = True

#     return has_lower and has_upper and has_digit and has_special

# password = input("Enter password: ")
# if validate_password(password):
#     print("Valid password")
# else:
#     print("Invalid password")