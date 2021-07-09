# 달리기

## 이중 반복문..기억 나시죠?

반복문은 아래와 같이 쓸 수 있죠?(반복문이 만약 기억안나신다면 걷기 단계에 있는 1차 반복문 문제를 풀고 와주세요.)

- python
```python
for i in range(0, 10):
  print(i)
```

- c/c++
```cpp
for(int i = 0; i < 10; i++) {
  printf("%d", i);
}
```

그럼 이중 반복문은 뭐였을까요?

반복문 안에 반복문을 넣는 것입니다! 간단하쥬?

그럼 한번 코드로 살펴볼게요.(python 기준으로만 작성할게요.)

```python
for i in range(0, 4):
  for j in range(0, 2):
    print(i, j)
```

위 코드의 출력 결과는 뭘까요? 아래를 보기 전에 한번 머리속으로 떠롤려보고 봐주세요!

```
0 0
0 1
1 0
1 1
2 0
2 1
3 0
3 1
```
과 같은 출력 결과가 나올거에요

왜?

```python
for i in range(0, 4): # 1번 반복문
  for j in range(0, 2): # 2번 반복문 이라고 부를게요!
    print(i, j)
```

1번 반복문에서 i가 0일때, 2번 반복문이 실행됩니다. 이때 2번 반복문에서 j가 0, 1로 순차적으로 변할거에요!

그럼 이 다음은 어떻게 되죠? i가 1 증가하고, 또 다시 2번 반복문에서 j가 0, 1로 순차적으로 변할거에요!

뭔가 어렵게 느낄 수 있지만 자연스럽게 `반복문은 안에 포함된 구문들을 반복한다! 설사 포함되어있는게 반복문일지라도!` 라고 생각하면 됩니다!

그럼 이제 이중 반복문을 활용한 문제들을 풀어볼게요.

## 1.먼저 이중 반복문을 단련해볼까요?
- [별 찍기 - 1](https://www.acmicpc.net/problem/2438)
- [별 찍기 - 2](https://www.acmicpc.net/problem/2439)
- [별 찍기 - 3](https://www.acmicpc.net/problem/2440)
- [별 찍기 - 4](https://www.acmicpc.net/problem/2441)
- [별 찍기 - 5](https://www.acmicpc.net/problem/2442)
- [별 찍기 - 6](https://www.acmicpc.net/problem/2443)
- [별 찍기 - 7](https://www.acmicpc.net/problem/2444)
- [별 찍기 - 8](https://www.acmicpc.net/problem/2445)
- [별 찍기 - 9](https://www.acmicpc.net/problem/2446)
- [별 찍기 - 12](https://www.acmicpc.net/problem/2522)
- [별 찍기 - 13](https://www.acmicpc.net/problem/2523)
- [별 찍기 - 14](https://www.acmicpc.net/problem/2556) (잘 추리해보시면 됩니다 ㅎㅎ 넘기셔도 됩니다)
- [별 찍기 - 15](https://www.acmicpc.net/problem/10990)
- [별 찍기 - 16](https://www.acmicpc.net/problem/10991)
- [별 찍기 - 17](https://www.acmicpc.net/problem/10992)
- [별 찍기 - 20](https://www.acmicpc.net/problem/10995)
- [별 찍기 - 21](https://www.acmicpc.net/problem/10996)
- [히스토그램](https://www.acmicpc.net/problem/13752)


## 소수와 관련된 문제를 풀어볼까요?
- [소수 찾기](https://www.acmicpc.net/problem/1978)
- [소수](https://www.acmicpc.net/problem/2581)

## 진법과 관련된 문제를 풀어볼까요?
- [9진수](https://www.acmicpc.net/problem/14491)
- [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)
- [이건 무슨 진법이지?](https://www.acmicpc.net/problem/13877)

## 기본적인 그리디 문제를 풀어볼게요!
- [우유 축제](https://www.acmicpc.net/problem/14720)

## 정렬에 대해 알아봅시다!

## 정렬을 쓰는 기본적인 문제를 풀어볼까요?

## 정렬을 쓰는 그리디 문제를 풀어볼게요

## 수학을 활용하는 문제를 풀어볼게요.
- [삼각형 외우기](https://www.acmicpc.net/problem/10101)
