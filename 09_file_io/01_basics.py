my_file = open("09_file_io/test-file.txt")

# cursor concept

print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)

print(my_file.read())
my_file.seek(0)


print(my_file.readline())
print(my_file.readline())

my_file.seek(0)

print(my_file.readlines())


my_file.close()
