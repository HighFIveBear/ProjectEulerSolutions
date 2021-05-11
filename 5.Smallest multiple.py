num = 20

while num > 0:
    div = 1
    x = 0
    while div <= 20:
        if num % div == 0:
            x = x + 1
        div = div + 1
    if x == 20:
        print(num)
        break
    print(num)
    num = num + 1