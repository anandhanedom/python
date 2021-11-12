# FOR loops
for alphabet in "hitman":
    print(alphabet)


for number in list(range(0, 10, 2)):
    print(number)


for item in (1, 2, 3, 4):
    for subItem in ("a", "b", "c"):
        print(f"{item}{subItem}")


for i, char in enumerate("Hello world"):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)


for i, number in enumerate(list(range(100))):
    if number is 50:
        print(number)

# WHILE loops

i = 0
while i < 50:
    print(i)
    i += 1
    # break - will skip else
else:
    print("Done looping till 49!")


for letter in "sdsd":
    pass  # thinking about it .......
