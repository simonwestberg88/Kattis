import sys
input = []

for x in sys.stdin:
    input.append(x)

X = int(input[0])
N = int(input[1])

budget = X*N

spent = 0
for x in range(2, N+2):
    spent += int(input[x])

left = budget - spent + X

print(str(left))
