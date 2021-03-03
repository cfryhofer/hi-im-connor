a = int(input())

b = int(input())

c = int(input())

d = int(input())

e = int(input())

f = int(input())


solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if x * a + y * b == c and x * d + y * e == f:
            print(x, y)
            solution = True

if not solution:
    print("No solution")
