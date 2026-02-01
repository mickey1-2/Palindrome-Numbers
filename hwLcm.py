num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
def calculate_lcm(num1, num2):
    greater = max(num1, num2)
    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            return greater
        greater += 1

print(calculate_lcm(num1, num2)) # Output: 60
