# 자전거

## 재귀함수란

![재귀함수](./img/what_is_recursive_function.png)

재귀함수는 말그래로 `재귀(본디의 곳으로 다시 돌아오는 것)` 하는 함수를 의미합니다.

그럼 어디로 돌아온다는 걸까요?

바로 자기 자신에게 돌아온다는 의미입니다. 뭔가 말이 이상하죠? 코드로 한번 봐보겠습니다.

```python
def f(n):
  print(n)
  f(n-1)
```

위 파이썬 코드는 f 라는 함수를 선언하고 있습니다. 어? 근데, f라는 함수에서 `f(n-1)` 을 호출하고 있는 모습이 보입니다.

처음에는 뭔가 이해가 안가는 구조일 수 있지만 f라는 함수에서 다른 함수도 아닌 자기 자신 f를 호출하고 있는데, 이걸 바로 재귀함수라고 합니다.

```python
만약 f(5) 를 호출했다고 해볼까요?

f(5)는 print(5)로 5를 출력하고, f(4)를 호출할 겁니다.

그럼 또, f(4)는 print(4)로 4를 출력하고, f(3)를 호출할 겁니다.

그럼 또, f(3)는 print(3)로 3을 출력하고, f(2)를 호출할 겁니다.

...

그럼 또, f(-1000000)는 print(-1000000)로 -1000000을 출력하고, f(-1000001)를 호출할 겁니다.

...

```

이렇게 계속 무한히 함수를 호출할 거고, 이는 무한 루프에 빠지게 됩니다.

그럼 어떻게해야 이 재귀 함수를 무한히 호출하지 않을까요?

바로 제한 조건을 추가해야합니다.

어떤식으로 하면 될까요? 예시를 한번 보겠습니다.

```python
def f(n):
  if n <= 0:
    return 0

  print(n)
  f(n-1)
```

위 파이썬 코드는 이전 예시와 비슷한 구조를 가지고 있습니다. 하지만, if문(조건문)이 추가된 모습을 볼 수 있습니다.
왜일까요? 이번에는 한번 f(3)을 호출한 상황을 살펴보겠습니다.

```python

f(3)는 print(3)로 3을 출력하고, f(2)를 호출할 겁니다.

그럼 또, f(2)는 print(2)로 2를 출력하고, f(1)를 호출할 겁니다.

그럼 또, f(1)는 print(1)로 1를 출력하고, f(0)를 호출할 겁니다.

여기서 잠깐!!!!!

f(0)이 호출되었을 때, 당연하게도 0이 출력될거라고 생각하셨나요?
0은 출력되지 않습니다. 왜냐? if(n<=0) 조건문에 걸려서 함수가 return(종료)되었기 때문입니다.

```

이해되셨나요?

이해가 되지 않으셨다면 위 코드를 한번 직접 작성해보고 실행해보시면 될 것 같아요 :D

(그래도 이해가 되지 않는다면 질문해주세요! 꼬오옥!)

> 이제 아래 문제들을 풀면서 재귀함수를 더 자세히 익혀봅시다!

## 재귀함수를 이용한 문제를 풀어볼까요?
- [[기초-재귀함수] 재귀로 * n개 한 줄로 출력하기](https://codeup.kr/problem.php?id=1851)
- [[기초-재귀함수] 재귀로 1부터 n까지 한 줄로 출력하기](https://codeup.kr/problem.php?id=1852)
- [[기초-재귀함수] 재귀로 1부터 n까지 합 리턴하기](https://codeup.kr/problem.php?id=1853)
- [[기초-재귀함수] 재귀로 각 자리 수의 합 리턴하기](https://codeup.kr/problem.php?id=1854)
- [[기초-재귀함수] 재귀로 n번째 피보나치 수 리턴하기](https://codeup.kr/problem.php?id=1855)
- [[기초-재귀함수] 계단 뛰어 오르기](https://codeup.kr/problem.php?id=1856)
- [[기초-재귀함수] 서로 다른 n개 중에서 r개 순서없이 고르기](https://codeup.kr/problem.php?id=1857)
- [[기초-재귀함수] 파스칼의 삼각형 출력하기 1](https://codeup.kr/problem.php?id=1858)
- [[기초-재귀함수] 별 삼각형 출력하기](https://codeup.kr/problem.php?id=1859)
- [[기초-재귀함수] 수 삼각형 출력하기](https://codeup.kr/problem.php?id=1860)
- [[기초-재귀함수] 파스칼의 삼각형 출력하기 2](https://codeup.kr/problem.php?id=1861)
- [[기초-재귀함수] 재귀로 n번째 피보나치 수 출력하기](https://codeup.kr/problem.php?id=1862)
- [(재귀 함수) 1부터 n까지 출력하기](https://codeup.kr/problem.php?id=1901)
- [(재귀 함수) 1부터 n까지 역순으로 출력하기](https://codeup.kr/problem.php?id=1902)
- [(재귀함수) 두 수 사이의 홀수 출력하기](https://codeup.kr/problem.php?id=1904)
- [(재귀함수) 1부터 n까지 합 구하기](https://codeup.kr/problem.php?id=1905)
- [(재귀함수) 팩토리얼 계산](https://codeup.kr/problem.php?id=1912)
- [(재귀함수) 피보나치 수열](https://codeup.kr/problem.php?id=1915)
- [(재귀함수) 2진수 변환](https://codeup.kr/problem.php?id=1920)
- [[재귀함수] 진법 변환](https://codeup.kr/problem.php?id=1921)
- [[재귀함수] 3n+1](https://codeup.kr/problem.php?id=1922)
- [(재귀함수) nCr (Small)](https://codeup.kr/problem.php?id=1925)
- [(재귀함수) 우박수 (3n+1) (basic)](https://codeup.kr/problem.php?id=1928)
- [(재귀함수) 삼각형 출력하기 1](https://codeup.kr/problem.php?id=1953)
- [(재귀함수)삼각형 출력하기 2](https://codeup.kr/problem.php?id=1954)
- [이진수 변환](https://www.acmicpc.net/problem/10829)
- [재귀함수가 뭔가요?](https://www.acmicpc.net/problem/17478)
- [별 찍기 - 10](https://www.acmicpc.net/problem/2447)
- [별 찍기 - 11](https://www.acmicpc.net/problem/2448)


## 진법 기억하시나요?



## 진법과 관련된 문제를 풀어볼까요?
- [9진수](https://www.acmicpc.net/problem/14491)
- [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)
- [이건 무슨 진법이지?](https://www.acmicpc.net/problem/13877)

## 스택을 활용한 문제를 풀어볼까요?


## 큐를 활용한 문제를 풀어볼까요?


## 해쉬를 이용한 문제를 풀어볼까요?


## 이제 자동차를 타러 가봅시다!

## 번외 문제
- [8진수 2진수](https://www.acmicpc.net/problem/1212)