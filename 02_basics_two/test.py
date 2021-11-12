picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


for row in picture:
    for binary in row:
        if binary:
            print("*", end="")
        else:
            print(" ", end="")
    print("")


some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]


i = 0
z = 0
dupicates = []
while i < len(some_list):
    z = i + 1
    while z < len(some_list):
        if some_list[i] is some_list[z]:
            dupicates.append(some_list[i])
        z += 1
    i += 1

print(dupicates)
