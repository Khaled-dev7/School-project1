n = 0

while n < 1 or n > 9:
    n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == n:
            print(j, end=' ')

        else:
            print(' ', end=' ')

    print()