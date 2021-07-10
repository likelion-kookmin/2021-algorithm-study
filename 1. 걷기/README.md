# 걷기 단계

## 0. 혹시 알고리즘 문제를 풀기로 결정한 언어 문법을 잘 모르시나요? 그럼 걸음마 단계에 있는 기초 100제 문제집을 먼저 풀어주세요!
[걸음마 단계 문제집](https://github.com/likelion-kookmin/2021-algorithm-study/tree/main/0.%20%EA%B1%B8%EC%9D%8C%EB%A7%88#2-%EC%A0%95%ED%95%9C-%EC%96%B8%EC%96%B4%EC%97%90-%EB%94%B0%EB%9D%BC-%EC%95%84%EB%9E%98-%EB%AC%B8%EC%A0%9C%EC%A7%91%EC%9D%84-%ED%92%80%EC%96%B4%EB%B4%85%EC%8B%9C%EB%8B%A4)

## 1. 기본적인 구현 문제를 풀어볼까요?
- [고양이](https://www.acmicpc.net/problem/10171)
- [A+B](https://www.acmicpc.net/problem/1000)
- [A/B](https://www.acmicpc.net/problem/1008)
- [사칙연산](https://www.acmicpc.net/problem/10869)
- [이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)
- [두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)
- [짝수와 홀수](https://programmers.co.kr/learn/courses/30/lessons/12937)
- [연세대학교](https://www.acmicpc.net/problem/15680)
- [세 수](https://www.acmicpc.net/problem/10817)
- [네 수](https://www.acmicpc.net/problem/10824)
- [최소, 최대](https://www.acmicpc.net/problem/10818)
- [치킨 두 마리 (...)](https://www.acmicpc.net/problem/14489)
- [시험 점수](https://www.acmicpc.net/problem/5596)
- [타임 카드](https://www.acmicpc.net/problem/5575) (hour(시간), minute(분)을 초(second)와 관련된 수식으로 나타낼 수 있을까요?)
- [과자](https://www.acmicpc.net/problem/10156)
- [쿠폰](https://www.acmicpc.net/problem/10179)
- [와글와글 숭고한](https://www.acmicpc.net/problem/17388)
- [사분면 고르기](https://www.acmicpc.net/problem/14681)
- [시험 성적](https://www.acmicpc.net/problem/9498)
- [특별한 날](https://www.acmicpc.net/problem/10768)
- [파일 옮기기](https://www.acmicpc.net/problem/11943)
- [과목 선택](https://www.acmicpc.net/problem/11948)


## 2. 1차 반복문을 이용한 구현 문제를 풀어볼까요?
- [제일 작은 수 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12935)
- [x만큼 간격이 있는 n개의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12954)
- [내적](https://programmers.co.kr/learn/courses/30/lessons/70128)
- [X보다 작은 수](https://www.acmicpc.net/problem/10871)
- [A+B - 3](https://www.acmicpc.net/problem/10950)
- [A+B - 5](https://www.acmicpc.net/problem/10952)
- [A+B - 7](https://www.acmicpc.net/problem/11021)
- [A+B - 8](https://www.acmicpc.net/problem/11022)
- [조교는 새디스트야!!](https://www.acmicpc.net/problem/14656)
- [상근날드](https://www.acmicpc.net/problem/5543)
- [10부제](https://www.acmicpc.net/problem/10797)
- [공](https://www.acmicpc.net/problem/1547)

## 3. 문자열을 알아볼까요?

문자열을 다룰 때는, 문자 한글자마다 배열에 담겨있다고 생각하고 접근을 하면 편합니다!

다만, 문자열은 프로그래밍 언어마다 살짝식 다르게 다루어집니다. (근본은 같지만..언어적인 특정에서 달라집니다.)

python에서의 문자열은 너무 간단하게 다룰 수 있습니다.

```python
a = "1234"
print(len(a)) # 문자열의 길이를 출력합니다.
print(a[0]) # 첫번째 문자를 출력합니다. 
```

C/C++에서의 문자열은 널문자에 대해 알아둘 필요가 있습니다.

널문자라는 건, `없는 문자`를 말합니다.

뭔가 이상한말이죠? 하지만 이 말이 맞는 말입니다. 진짜 아무것도 없다라는 것을 의미해요.

그럼 공백과 다를게 뭐냐라고 이야기할 수 있어요.

아래 사진이 두 개의 차이에 도움이 될 것 같아요.

![널과 공백](./img/empty_string_and_null.jpeg)

이해가 되셨나요?

그럼 널을 왜 설명했냐?를 말하기전에 아래 표를 볼게요.

| 주소 |0|1|2|3|4|5|6|7|8|9|10|11|12|13|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| 문자열 | k| o | o | k | m | i | n | h|e|l|l|o|||

위 표와 같이 어떤 저장공간에 순서대로 kookmin과 hello라는 단어가 담겨있다고 해볼게요.

근데, 한가지 문제가 있어보입니다.

컴퓨터는 kookmin과 hello라는 단어는 어떻게 구분이 되야할까요?

컴퓨터가 잘못 구문하면 kook, min, hello가 될 수도 있고 kookminhell, o가 될 수도 있는것이죠.

그럼 이걸 구분 지을 수 있기 해주어야겠죠?

| 주소 |0|1|2|3|4|5|6|7|8|9|10|11|12|13|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| 문자열 | k| o | o | k | m | i | n | 0(널문자) |h|e|l|l|o| 0(널문자)|

단어의 끝마다 널문자를 하나씩 더 넣어주면, 자연스럽게 컴퓨너는 "아! 널문자전까지가 이 문자열이구나!" 하고,

kookmin, hello를 구분할 수 있게 됩니다.

이걸 알아두시고, C/C++에서의 문자열의 문법들을 공부하고 아래 문제들을 풀어보면 좋을 것 같아요 :D

## 3-1. 문자열을 이용한 간단한 문제를 풀어볼까요?
- [문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918)
- [가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)
- [이상한 문자 만들기](https://programmers.co.kr/learn/courses/30/lessons/12930)
- [모음의 개수](https://www.acmicpc.net/problem/10987)
- [모음의 개수](https://www.acmicpc.net/problem/1264)
- [단어 뒤집기](https://www.acmicpc.net/problem/9093)
- [대소문자 바꾸기](https://www.acmicpc.net/problem/2744)
- [등장하지 않는 문자의 합](https://www.acmicpc.net/problem/3059)

## 3-2. 문자열을 이용한 조금 심화된 문제를 풀어볼까요?
- [뒤집힌 덧셈](https://www.acmicpc.net/problem/1357)
- [카이사르 암호](https://www.acmicpc.net/problem/5598)
- [야바위 대장](https://www.acmicpc.net/problem/15814)
- [아!](https://www.acmicpc.net/problem/4999)
- [가장 많은 글자](https://www.acmicpc.net/problem/1371) (EOF에 대해 먼저 알아보기!)
- [연속구간](https://www.acmicpc.net/problem/2495)
- [민균이의 비밀번호](https://www.acmicpc.net/problem/9933)
- [지영 공주님의 마법 거울](https://www.acmicpc.net/problem/11586) (구현 능력 연습하기!)
- [나는 친구가 적다 (Small)](https://www.acmicpc.net/problem/16171) (미리 맛보는 그리디)

## 4. 이제 한번 달려봅시다! 달리기 단계로 이동해볼까요 😄

## 번외문제
- [나이 계산하기](https://www.acmicpc.net/problem/16199)
- [카드 뽑기](https://www.acmicpc.net/problem/16204)
- [베시와 데이지](https://www.acmicpc.net/problem/16431)
