# import sys
# n = int(sys.stdin.readline())
# L = [int(sys.stdin.readline()) for i in range(n)]
"""
python으로 이 문제를 풀려면, 위 입력 방식을 사용해야 합니다.
python의 기본 입출력이 너무 느리기에... 이 문제에서는 어쩔 수 없이 이 방식을 사용해야 하고,
일단 아래 코드와 같다고 생각해주시면 됩니다.
"""

n = int(input())
L = [int(input()) for i in range(n)]

stk = []

"""
놀랍게도, python에서는 리스트를 이용해서
간단하게 stack을 사용할 수 있습니다.

push의 개념은 append()로
top의 개념은 stk[-1]로
pop의 개념은 pop()으로
size의 개념은 len(stk)로 말이죠.
"""

for i in range(0, n):
  crt = L[i]
  if len(stk) == 0: # stack이 비어있다면,
    stk.append(L[i]) # stack에 그래도 값을 push한다.
  else: # stack에 값이 들어가 있다면,
    while len(stk) > 0 and stk[-1] < crt: # stack에 값이 있고, stack의 top이 현재값과 같거나 작으면, 계속해서
      stk.pop() # pop한다.
    stk.append(crt) # 이제 왼쪽에 현재값보다 작은 값이 없기 때문에 push한다.
print(len(stk))
