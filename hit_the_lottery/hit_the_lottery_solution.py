#!/usr/bin/python3

n = int(input())
count = 0

while n // 100 != 0:
    if n % 100 == 0:
        count = n // 100
        n = 0
    else:
        count += n // 100
        n %= 100
if n // 20 != 0:
    count += n // 20
    n %= 20
if n // 10 != 0:
    count += n // 10
    n %= 10
if n // 5 != 0:
    count += n // 5
    n %= 5
while n != 0:
    count += 1
    n -= 1

print(count)
