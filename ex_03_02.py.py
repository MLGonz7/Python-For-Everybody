score = input("Enter Score:")
sf = float(score)


if sf > 1.0 or sf < 0:
    print("Error, grade is outside of acceptable range")
elif sf >= 0.9:
    print ("A")
elif sf >= 0.8:
    print("B")
elif sf >= 0.7:
    print("C")
elif sf >= 0.6:
    print("D")
elif sf < 0.6:
    print("F")
