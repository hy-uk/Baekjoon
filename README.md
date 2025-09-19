# 백준 문제풀이 후 노트정리

***항상 문제 풀고 구글링해서 내가 쓴 답과 다른 사람이 쓴 답이 어떻게 다른지 확인하기***

### 1000
* **map 함수 기본형 > map(적용할 함수,반복 가능한 자료형)**
```py
a,b=map(int,input().split())
print(a+b)
또는
a,b=input().split()
print(int(a)+int(b))
```

### 10869
* 정수인 몫을 구할 때는 int(a/b)도 되지만 '//' 자체가 몫을 구하는 연산자임

### 10926 
<img width="50%" height="50%" alt="스크린샷 2025-09-19 120534" src="https://github.com/user-attachments/assets/698506b8-c131-421f-a840-e9c21e2e345c" />

* input은 언급이 없으면 'str'로 받기 때문에 ','로 잇는 것이 아닌 +로 두 문장을 합쳐줌
* print(input()+"??!")로도 풀이 가능
* 문제 풀 때 변수를 a로 설정했는데 앞으로는 변수가 뭘 의미하는지 알 수 있도록 설정하기 가령 이 문제에서는 a > id로 설정

### 10430
* 나머지를 구해서 곱하는 방식도 괜찮지만 input을 활용해 문자열 그 자체로 받아서
백의자리, 십의자리, 일의자리를 각각 하나씩 생각해서 곱하는 방법도 있음
```py
A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
```
