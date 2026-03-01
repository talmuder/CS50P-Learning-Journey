score=int(input("Score: "))
#grade tier
if 100 >= score >= 90:
    print("Grade: A")
elif 90 > score >= 80:
    print("Grade: B")
elif 80 > score >= 70:
    print("Grade: C")
elif 70 > score >= 60:
    print("Grade: D")
else:
    print("Grade: F")