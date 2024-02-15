#question 5: Reverse Integer
reversed_num = 0
num = int(input("Enter Number: "))
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))