f = open("C:\\git\kattis\\What does the fox say\\b-sample.in", "r")

input = f.readlines()

T = input[0]

saidWords = input[1].split(" ")
saidWords[len(saidWords)-1] = saidWords[len(saidWords)-1].replace("\n", "")

words = []

for i in range(2, len(input) -1):
    split = input[i].split(" ")
    words.append(split[2].replace("\n", ""))

fox = []
for x in saidWords:
    if (x not in words):
        fox.append(x)

for x in fox:
    print(x, end = " ")