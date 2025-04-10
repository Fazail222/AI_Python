import random

# 1 Temperature Converter c to f or f to cel
def temp(val, u):
    result = 0
    if a== 'cel':
        result = (val * 9 / 5) + 32
        print(str(result) + 'Ferenheight')
    elif a== 'feren':
        res = (val - 32) * 5 / 9
        print(str(res) + 'Celcieus')

temp(60, 'cel')
temp(45, 'feren')

# 2 Find  the numbers divisible by both 5 and 7
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n)

#3 Number Guess
num = random.randint(1, 9)
while True:
    a = int(input("Guess a number between 1 and 9: "))
    if a == num:
        print("Well guessed!")
        break
    else:
        print(" You Are Wrong!")

#4 Pattern printing
n = 5
s = 1
flag = False
for r in range(0, 2 * n):
    for _ in range(0, s):
        print("*", end="")
    print("")
    if s < n and not flag:
        s += 1
    elif s == n and not flag:
        flag= True
        s -= 1
    else:
        s -= 1

#5 Reverse string 
word= input("Enter a word: ")
print(word[::-1])


#6 Count even and odd
lst = [1, 5, 6, 20, 30, 11]
even = 0
odd = 0
for x in lst:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

#7 Show type of each item
data = [7893, 4.55, 4+5j, false, "Hello there", (7, 4), [2, 5], {"a": 1, "b": 2}]
for x in data:
    print(x, type(x))

#8 Skip certain numbers
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=" ")

#9 Fibonacci until >50
a = 0
b = 1
while True:
    print(a)
     a = b
     b=a + b
    if b > 50:
        break

#10 2D list value assign
i = 4
j = 3
mat = [[0]*5 for _ in range(5)]
mat[i][j] = 99
print(mat)

