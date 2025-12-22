# 1330
A,B = map(int,input().split())

if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")


# 9498
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# 2753 *MD
year = int(input())

if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(1)
else:
    print(0)


# 14681
x=int(input())
y=int(input())

if x>0:
    if y>0:
        print(1)
    elif y<0:
        print(4)
else:
    if y>0:
        print(2)
    elif y<0:
        print(3)


# 2884 *MD
hour,min=map(int,input().split())

if min-45>=0:
    print(hour,min-45)
else:
    if hour>0:
        print(hour-1,min+15)
    else:
        print(23,min+15)


# 2525 *MD
hour,min=map(int,input().split())
time=int(input())

if min+time<60:
    min+=time
else:
    hour+=(min+time)//60
    min=(min+time)%60
    if hour>=24:
        hour-=24
print(hour,min)


# 2480
a,b,c=map(int,input().split())

if a==b==c:
    award=10000+1000*a
elif a==b:
    award=1000+100*a
elif b==c:
    award=1000+100*b
elif a==c:
    award=1000+100*a
else:
    award=100*(max(a,b,c))

print(award)


# 2739
N=int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")


# 10950
test_case=int(input())
for i in range(test_case):
    a,b=map(int,input().split())
    sum=a+b
    print(sum)


# 8393
n=int(input())
sum=0

for i in range(1,n+1):
    sum+=i

print(sum)


# 25304
total=int(input())
number=int(input())
sum=0

for i in range(number):
    price,num=map(int,input().split())
    sum+=price*num

if sum==total:
    print("Yes")
else:
    print("No")


# 25314
N=int(input())

print("long",end=" ")     # 다른 풀이: print(N//4*"long "+"int")

print("int")


# 2438        # 파이썬은 문자열*N이 가능하므로 기억하고 잘 쓰기 (위 문제에서도 적용가능)
N=int(input())

for i in range(N):
    for j in range(i+1):
        print("*",end="")
    print(  )


# 2439
N=int(input())

for i in range(N):
    print(" "*(N-1-i),end="")
    print("*"*(i+1))


# 10952
while 1:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)


# 10951     # 무한루프 반복문이고 if-break가 아닌 오류로 인한 break를 걸 때 try-except 사용
while 1:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break
