num = int(input("Enter a number: "))

temp = num
count = 0

# Find length of the number
while temp > 0:
    count += 1
    temp //= 10

temp = num
sum = 0

# Separate digits and calculate power
while temp > 0:
    digit = temp % 10
    print("Digit =", digit)
    sum += digit ** count
    temp //= 10

print("Sum =", sum)

# Check condition
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")