#include <iostream>
#include <stack>
using namespace std;
// 직접 stack을 구현해서 써도 되지만, STL의 stack을 써서 더 편하게 문제 풀이를 해볼게요. 

// 과연 아래 풀이가 정말 최적일까요? 더 간단하게 풀 수 있는 방법은 없을까요? 한번 생각해보시면 좋을 것 같아요.

bool isVPS(string s) {
  stack<char> stk; // 스택 선언

  for(int i = 0; i < s.length(); i++) { // 문자열을 앞에서부터 쭉 탐색합니다.
    if(s[i] == '(') { // 만약 현재 문자가 ( 여는 괄호 문자라면,
      stk.push(s[i]); // 바로 스택에 넣어줍니다.
    } else if(s[i] == ')') { // 만약 현재 문자가 ) 닫는 괄호 문자라면,
      if(stk.size() == 0) return false; // 현재 스택에 쌓여있는 ( 여는 문자가 없다면, 이는 VPS가 아닙니다.
      stk.pop(); // 현재 스택에 쌓여있는 ( 여는 문자가 있다면, 짝이 맞는 괄호가 있다는 의미이므로 stack에서 ( 를 하나 제거합니다.
    }
  }
  if(stk.size() > 0) return false; // 모든 문자열을 훑었는데도, ( 여는 문자가 남아있다면 이는 VPS가 아닙니다.
  return true; // 모든 제한 조건을 통과하였으니, 이는 VPS입니다. 
}

int main() {
  int N;
  string s;
  cin >> N;
  for(int i = 0; i < N; i++) {
    cin >> s;
    cout << (isVPS(s) ? "YES" : "NO") << "\n";
  }

  return 0;
}
