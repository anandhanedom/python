class SuperList(list):
    def __len__(self):
        return 1000


superlist1 = SuperList()


superlist1.append(1)
superlist1.append(2)
superlist1.append(2)


print(len(superlist1))
print(superlist1[0])


print(issubclass(SuperList, list))  # SUBCLASS check
