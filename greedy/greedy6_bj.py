#백준11047번_동전0 (2022.01.23)

import sys
n, k = map(int,sys.stdin.readline().split())
money = []
result = 0

for i in range(n):
  a = int(sys.stdin.readline())
  money.append(a)

money.sort(reverse=True)

for i in money:

  if k == 0:
    break

  if k >= i:
    result += (k//i)
    k = (k % i)

print(result)

