# A. Wrong Subtraction
|Rules | Limits|
|--------------------|----------|
|time limit per test | 1 second | 
|memory limit per test | 256 megabytes |
|input | standard input |
|output | standard output |

Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a 
number consisting of two or more digits. Tanya subtracts one from a number by the following algorithm:

    if the last digit of the number is non-zero, she decreases the number by one;
    if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit). 

You are given an integer number n. Tanya will subtract one from it k times. Your task is to print the 
result after all k subtractions.

It is guaranteed that the result will be positive integer number.

Input

The first line of the input contains two integer numbers nand k (2≤n≤109, 1≤k≤50) — the number from 
which Tanya will subtract and the number of subtractions correspondingly.

Output

Print one integer number — the result of the decreasing n by one k times.
It is guaranteed that the result will be positive integer number. 

i.e.
| input        | output |
|--------------|--------|
| 512 4        | 50     |
| 1000000000 9 | 1      |


Note
The first example corresponds to the following sequence: 512→511→510→51→50.
  
### Explaining the problem:
Giving a number n and a number k where k = number of times of the process.
If n ends with 0 you must eliminate the 0. If n ends with any number between 
1-9 you must subtract 1. 
Examples:

| input | output |
|-------|--------|
|n=256 k=5|result=251|
|n=154 k=5|result=15|

REFERENCE:
https://codeforces.com/contest/977/problem/A
