from itertools import permutations
import math
n = input("Enter the number of Chairs:\n")
n = int(n)
a = []
for i in range(1, n+1):
    a.append(i)
tot = math.factorial(len(a))
p = list(permutations(a))
k = 0
for i in p:
    f = 0
    for m in range(len(i)):
        if i[m] == m+1:
            f = 1
            break
    if f == 0:
        k = k+1
print("Total Possible Ways = " + str(tot))
print("Our Arrangements = " + str(k))
