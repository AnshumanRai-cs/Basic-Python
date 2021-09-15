number = int(input("Enter any Number : "))
print("Prime number between", 1 ,"and", number,"are")
for num in range(1, number+1):
    if num > 1:
        for i in range(2, num):
            if(num % i)== 0:
                break
        else:
            print(num)