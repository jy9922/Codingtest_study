a = list(map(int, input()))
result = 0

#두 숫자 중 하나가 0 이거나 1이면 곱보다는 더하기 수행
for i in a:
  if i <= 1 or result <= 1:
    result += i
  else:
    result *= i


print(result)
