import time
u = int(input('How many entries in a list you want: '))
u = u-1
qwe = u+1
i = -1
x = [u]
while i < u:
    i = i+1
    k = x[i]
    k = int(input(f'Enter number to store at position of {i+1} : '))
    if qwe >= 0:
        print('Remaining entries :', qwe-1)
        qwe = qwe-1
    else:
        print('All entries used ')
    x.append(k)

x.remove(u)

# print(x)
# x.sort()
# print('Sorted form of data goes here:')
# print(x)

ol = x.copy()
x.sort()
z = len(x)
# q = int(input('Enter time delay: '))
q = 1
p = 0
while p <= q:
    time.sleep(q)
    p = p+1
    print('........................'"\n")
# ranging from {x[0]} to {z}
y = int(input(f'Enter a  integer to find from the data you entered: '))
while p <= q:
    time.sleep(q)
    p = p+1


time.sleep(q)
print('Number entered is found in list(s)')
while p <= q:
    time.sleep(q)
    p = p+1
    print('.'"\n")
i = -1
while i <= z:
    i = i+1
    k = x[i]
    if y == k:
        print('------------------------------------------------')
        print('------------------------------------------------')
        # as lists start from 0 not from 1
        print('List sorted')
        print(
            f'Founded {y} in sorted list at position of {i+1} displayed below\n ')
        print('------------------------------------------------')
        print('------------------------------------------------')
        print('Sorted list(s) here')
        print(x)
        print('------------------------------------------------')
        print('Here you got your data as entered by user  :( #Unsorted ')
        print('------------------------------------------------')
        print(ol)
        print('------------------------------------------------')
        print('------------------------------------------------')
        print('You can cross check from above ')
        print('BYE BYE ')
        break
    else:
        pass
