#백준11399번_ATM (2022.01.22)

import sys
num = int(sys.stdin.readline())
person = list(map(int,sys.stdin.readline().split()))
money_time = 0
sum_time = 0

person.sort()
for i in person:
  money_time += i
  sum_time += money_time

print(sum_time)