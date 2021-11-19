a = 10


# def something():
#     global a
#     a = 11
#     print(f"Local : {a}")
# something()

# with same name
def something():
    a = 9
    x = globals()["a"]
    print(f"Global inside local before updation:{x}")
    globals()["a"] = 20
    print(f"Local : {a}")


something()
print(f"Global : {a}")
