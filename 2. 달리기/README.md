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

## 정렬에 대해 알아봅시다!

정렬은 뭘까요?

이중 반복문하다가 갑자기 정렬이 뭐냐!라고 하니 당황스러우실 수 있습니다.

다만.. 정렬은 한번 뚫고 지나가야할 하나의 관문입니다. 그래서 달리기하는 도중 꼭 지나쳐야 하는 곳입니다.

정렬은 흔히 알고 있듯이 순서대로 나열하는 것입니다. 그럼 왜 정렬을 하고, 컴퓨터는 어떻게 정렬할까요?

### 정렬은 왜 할까요?

일단 정렬을 하면 데이터를 다루는게 편해집니다.

예를 한번 들어볼까요?

`10 0 2 11 21 2 4 1 123 44 22 23`

이중 5번째로 큰 숫자는 무엇일까요?

아마 여러분들 대부분은 큰 숫자부터 찾아가면서 5번째로 큰 숫자를 찾았을 겁니다.

그럼 이걸 컴퓨터로(코드로) 한번 바꾸어볼까요?

```python
L = [10, 0, 2, 11, 21, 2, 4, 1, 123, 44, 22, 23]

for i in range(4):
  max_value = max(L) # 최대값을 찾아줍니다.
  L.remove(max_value) # 최대값을 제거합니다.

print(max(L)) # 가장 큰 숫자부터 4개의 숫자를 제거했기 때문에 남은 숫자가 5번째로 큰 숫자입니다. -> 21
```

아마 사람이 생각하는 과정을 코드로 나열하면 이런 코드로 나타낼 수 있을 겁니다.

하지만, 만약 정렬이 되어있었다면?

```python
L = [0, 1, 2, 2, 4, 10, 11, 21, 22, 23, 44, 123]

print(L[-5]) # 뒤에서 5번째에 있는 값을 출력합니다.
```

너무나도 쉽게 이 문제가 해결됩니다.

이 예시 말고도, 여러 상황에서 정렬이 활용되고, 추가자료에서 다루는 "시간복잡도"를 개선하기 위해서도 정렬은 많이 활용됩니다.

어렵더라도 익힐 필요가 보이시나요? 😁

### 정렬은 어떻게 쓰나요?

일단 정렬을 활용하는 코드를 작성할 때, 직접 구현하셔도 됩니다.
물론 열심히 이중 반복문을 배운 여러분은 아래와 같은 정렬 코드를 작성하실 수 있을거라고 생각이 들어요.

TODO: 버블 소트 추가
```
```

이런 코드를 버블 소트라고 합니다. (아래 이미지와 같이 숫자가 옮겨지는 과정이 거품이 점점 수면으로 올라오는 모습과 닮아서 그렇다고 합니다. ~~솔직히 전 딱히 그렇게 느껴지지는 않는데 여러분은 어떠신가요?~~ )


TODO: 이미지 추가

버블 소트 말고도, 엄청나게 많은 정렬 알고리즘이 존재합니다.

병합 정력, 퀵 정렬, 타노스 정렬(?!), ... 

정렬 알고리즘들은 각각의 장점과 단점이 존재하고, 구현 방식이 다르기도 하고,

각 정렬 알고리즘마다 걸리는 시간, 사용하는 메모리의 양이 다릅니다. 그럼 상황에 맞춰서 정렬 알고리즘을 선택해야겠죠? (어떻게 다른지는 직접 찾아보시면서 알아봐주세요!)

하지만, 대부분의 프로그래밍 언어에서는 기본적으로 최적화된 정렬 알고리즘을 사용할 수 있게 해줍니다.

예를 들자면, (l 이 정렬하려는 리스트 혹은 배열일 때) python에서는 l.sort(), C/C++(STL)에서는 sort(l, l+10)와 같이 사용할 수 있습니다.

따라서, 어지간해서는 알고리즘 문제를 푸실때는 주어지는 sort 함수/메서드를 활용하시면 됩니다.

> 참고) 아래 정렬 알고리즘이 가시화된 영상을 보시면서 어떤 정렬이 빠른지 보시면 될 것 같습니다. 영상 좌상단에 정렬 알고리즘의 이름이 표시됩니다. ㅎㅎ

[![15 Sorting Algorithms in 6 Minutes](https://img.youtube.com/vi/kPRA0W1kECg/0.jpg)](https://www.youtube.com/watch?v=kPRA0W1kECg&ab_channel=TimoBingmann)

## 정렬을 활용하는 문제들을 풀어볼까요?

- [세수정렬](https://www.acmicpc.net/problem/2752) : 정렬 part이긴 하지만 정렬을 안쓰고도 해결할 수 있을까요?
- [거북이](https://www.acmicpc.net/problem/2959)
- [콘테스트](https://www.acmicpc.net/problem/5576)
- [수 정렬하기](https://www.acmicpc.net/problem/2750)
- [애너그램](https://www.acmicpc.net/problem/6996)
- [단어 퍼즐](https://www.acmicpc.net/problem/9946)
- [단어 정렬](https://www.acmicpc.net/problem/1181)
- [등수 구하기](https://www.acmicpc.net/problem/1205)
- [소트인사이드](https://www.acmicpc.net/problem/1427)
- [도비의 난독증 테스트](https://www.acmicpc.net/problem/2204) : 어떻게 하면 대소문자를 구분하지 않고 정렬할 수 있을까요?
- [N번째 큰 수](https://www.acmicpc.net/problem/2693)
- [수 정렬하기 2](https://www.acmicpc.net/problem/2751)
- [점수 계산](https://www.acmicpc.net/problem/2822)
- [수학숙제](https://www.acmicpc.net/problem/2870)
- [종이자르기](https://www.acmicpc.net/problem/2628)
- [아시아 정보올림피아드](https://www.acmicpc.net/problem/2535) : python에서는 리스트 혹은 튜플을 정렬하면 되지만... C/C++에서는 구조체를 활용해야겠죠?

## 그리디 문제란?



## 기본적인 그리디 문제를 풀어볼게요!
- [우유 축제](https://www.acmicpc.net/problem/14720)
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()

## 정렬을 쓰는 그리디 문제를 풀어볼게요
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()


## 잠깐! 수학을 활용하는 문제를 풀어볼게요.
- [삼각형 외우기](https://www.acmicpc.net/problem/10101)
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()


## 소수를 코드로 어떻게 알아낼까?




## 소수와 관련된 문제를 풀어볼까요?
- [소수 찾기](https://www.acmicpc.net/problem/1978)
- [소수](https://www.acmicpc.net/problem/2581)
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()
- []()