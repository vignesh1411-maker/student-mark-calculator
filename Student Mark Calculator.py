name = input("Enter student name:")

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
social = int(input("Enter Social mark: "))

total = tamil + english + maths + science + social

average = total / 5

print("Total =", total)
print("Average =", average)

if average >= 90:
    print("Grade A")

elif average >= 70:
    print("Grade B")

elif average >= 50:
    print("Grade C")

else:
    print("Fail")

if tamil >= 35 or english >= 35 or maths >= 35 or science >= 35 or social >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
