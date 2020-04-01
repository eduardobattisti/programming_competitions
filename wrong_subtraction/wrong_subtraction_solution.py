#!/usr/bin/python3    

# we create a 2 variables with the function map. Which expect a input 
# of two values and then these values are splited into the 2 variables;

n, k = map(int, input().split())

# k is the number of times we want to subtract the number, so we use a
# for loop to pass through n times k. Then we establish a condition. n just will 
# be n - 1 if n isn't divisible by 10, else n will be divide by 10;

for i in range(k): n = n-1 if n % 10 != 0 else n // 10
print(n)


