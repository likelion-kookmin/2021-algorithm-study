"""
  1부터 입력이 들어오는 수까지 소수 목록을 뽑는 코드입니다.
"""

a = int(input())
ret = [] # result 의 약어입니다. 종종 쓰이는 변수명이에요. 

for i in range(2, a+1):
  for j in range(2, i):
    if i % j == 0: # 나누어떨어지면 소수가 아니고, 약수가 존재한다는 것!
      break
  else:
    ret.append(i)

print(ret) # 결과를 출력합니다.
