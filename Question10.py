n = int(input("Enter the Limit"))
x= float(input("Enter Power of e"))
p=1
f=1
s=1
for i in range (1,n+1):
    p=p*x
    f=f*i
    s =s+(p/f)
print(round(s,2))