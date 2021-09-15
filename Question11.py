rows = 4
for i in range(rows, 1, -1):
    num = i
    for j in range(1, i):
        print(j, end=' ')
    print("\r")
