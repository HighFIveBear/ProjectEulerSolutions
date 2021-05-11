a = 1
b = 1
c = 0
list1 = []

while a < 1000:
    while b < 1000:
        c = a * b
        list1.append(c)
        b = b + 1
    b = 1
    a = a + 1
list1.sort()
list1.reverse()

for num in list1:
    x = num
    rem = 0
    rev = 0
    while x > 0:
        rem = x % 10
        rev = rev * 10 + rem
        x = x // 10
    if rev == num:
        print(rev)
        break