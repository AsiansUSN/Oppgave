namelist = []
for i in range(3):
    name = input('Name Number ' + str(i + 1) + ' ')
    namelist = namelist + list([name])
print(namelist)

namelist.sort()
print(namelist)

namelist.reverse()
print(namelist)