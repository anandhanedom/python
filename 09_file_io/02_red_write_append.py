with open("09_file_io/test-file.txt") as my_file:
    print(my_file.readlines())

# with open("test-file.txt", mode="r+") as my_file:
#     new_text = my_file.write("hey hello world!")
#     print(new_text)

with open("09_file_io/test-file.txt", mode="a") as my_file:
    new_text = my_file.write("hey hello worldsssss!")
    print(new_text)


try:
    with open("test.js", mode="r") as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print("File does not exist", err)

except IOError as err:
    print("File does not exist")
    raise err
