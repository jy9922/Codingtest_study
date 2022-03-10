#백준2839번_설탕배달

import sys
s = int(sys.stdin.readline())

result = 0

while True:
  if s % 5 == 0:
    result += (s//5)
    break
  s -= 3
  result += 1
  if s < 0:
    result = -1
    break

print(result)