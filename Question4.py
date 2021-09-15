print("Enter Marks Obtained in 5 Subjects :")
subject1 = int(input())
subject2 = int(input())
subject3 = int(input())
subject4 = int(input())
subject5 = int(input())
avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
if avg >85 and avg<100:
    print("Your Grade is A")
elif avg >70 and avg <85:
    print("Your Grade is B")
elif avg >60 and avg<69:
    print("Your Grade is C")
elif avg >45 and avg<59:
    print("Your Grade is D")
elif avg<45:
    print("Your Grade is E")
else:
    print("Invalid Input!")