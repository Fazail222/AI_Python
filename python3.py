import random

# Temperature Converter
def conv_temp(val, u):
    res = 0
    if u == 'c':
        res = (val * 9 / 5) + 32
        print(str(res) + 'F')
    elif u == 'f':
        res = (val - 32) * 5 / 9
        print(str(res) + 'C')

conv_temp(60, 'c')
conv_temp(45, 'f')

# Find numbers divisible by both 5 and 7
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n)

# Number Guessing Game
num = random.randint(1, 9)
while True:
    g = int(input("Guess a number between 1 and 9: "))
    if g == num:
        print("Well guessed!")
        break
    else:
        print("Wrong!")

# Pattern printing
n = 5
s = 1
maxed = False
for r in range(0, 2 * n):
    for _ in range(0, s):
        print("*", end="")
    print("")
    if s < n and not maxed:
        s += 1
    elif s == n and not maxed:
        maxed = True
        s -= 1
    else:
        s -= 1

# Reverse string (slice method)
w = input("Enter a word: ")
print(w[::-1])

# Reverse string (loop method)
w = input("Enter a word: ")
rev = ""
for i in range(1, len(w) + 1):
    rev += w[-i]
print(rev)

# Count even and odd
lst = [1, 3, 12, 14, 35, 24]
even = 0
odd = 0
for x in lst:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Show type of each item
data = [123, 1.24, 1+2j, True, "Hi", (2, 5), [2, 5], {"a": 1, "b": 2}]
for x in data:
    print(x, type(x))

# Skip certain numbers
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=" ")

# Fibonacci until >50
a = 0
b = 1
while True:
    print(a)
    a, b = b, a + b
    if b > 50:
        break

# 2D list value assign
i = 4
j = 3
mat = [[0]*5 for _ in range(5)]
mat[i][j] = 99
print(mat)