n = int(input("Enter the number:"))
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(3 * n + 1)
    print(n)

print(n)