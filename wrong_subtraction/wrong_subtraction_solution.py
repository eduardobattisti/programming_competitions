#!/usr/bin/python3    
     
''' 
Explaining the problem:
Giving a number n and a number k where k = number of times of the process.
If n ends with 0 you must divide it by 10, to eliminate the 0. If n ends with
any number between 1-9 you must subtract 1. 
Examples:
n=256 k=5         |n=154 k=5
result=251        |result=15
'''

n, k = map(int, input().split())
     
for i in range(k): n = n-1 if n % 10 != 0 else n // 10
print(n)

# Line 3 - we create a 2 variables with the function map. Which expect a input 
# of two values and then these values are splited into the 2 variables;

# Line 5 - k is the number of times we want to subtract the number, so we use a
# for loop to pass through n times k. Then we establish a condition. n just will 
# be n - 1 if n isn't divisible by 10, else n will be divide by 10;