largest=int(input("Enter your largest number:"))
smallest=int(input("Enter your smallest number:"))
while (smallest):
    numstore=smallest
    smallest=largest%smallest
    largest=numstore
print("HCF is",largest)