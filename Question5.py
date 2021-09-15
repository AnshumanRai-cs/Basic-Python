nterms = int(input("How many terms? "))

number1, number2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(number1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(number1)
       nth = number1 + number2
       number1 = number2
       number2 = nth
       count += 1