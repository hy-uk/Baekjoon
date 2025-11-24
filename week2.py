# # 1330
# A,B = map(int,input().split())

# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# else:
#     print("==")

# # 9498
# score = int(input())

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# # 2753
# year = int(input())

# if year%4 == 0 and (year%100 != 0 or year%400 == 0):
#     print(1)
# else:
#     print(0)

# # 14681
# x=int(input())
# y=int(input())

# if x>0:
#     if y>0:
#         print(1)
#     elif y<0:
#         print(4)
# else:
#     if y>0:
#         print(2)
#     elif y<0
#         print(3)

# # 28
# hour,min=map(int,input().split())

# if min-45>=0:
#     print(hour,min-45)
# else:
#     if hour>0:
#         print(hour-1,min+15)
#     else:
#         print(23,min+15)

# # 2525
# hour,min=map(int,input().split())
# time=int(input())

# if min+time<60:
#     min+=time
# else:
#     hour+=(min+time)//60
#     min=(min+time)%60
#     if hour>=24:
#         hour-=24
# print(hour,min)

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