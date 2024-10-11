mylist = [9, 0, 0, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
while i < len(mylist):
    if mylist[i] == 0:
        mylist.append(mylist[i])
        mylist.remove(mylist[i])
    i += 1
print(mylist)