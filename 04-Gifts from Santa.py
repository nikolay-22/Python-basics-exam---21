n = int(input()) # N – цяло число – 0 <= N < M
m = int(input()) # M – цяло число – N < M <= 10000
s = int(input()) # S – цяло числo – N <= S <= M

for number in range (m, n - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number != s:
            print(number, end = " ")
        else:
            break