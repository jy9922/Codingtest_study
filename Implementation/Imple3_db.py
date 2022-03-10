#현재 나이트의 위치
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#ord(문자) 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환 [ord('a')를 넣으면 정수 97 반환]]

#나이트가 이동할 수 있는 8가지 방향
steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지
result = 0
for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]