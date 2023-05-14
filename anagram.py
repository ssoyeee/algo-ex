import sys

sys.stdin=open("input.txt","r")

a=input()
b=input()

str1=dict()
str2=dict()

for x in a: #a 문자열 하나하나가 x에 대응
    str1[x] = str1.get(x, 0)+1

for x in b:
    str2[x] = str2.get(x, 0)+1

for i in str1.keys(): # str1의 key값들 다 방문
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    
    else:
        print("NO")
else: 
    print("YES")


# 개선된 코드
# import sys

# sys.stdin=open("input.txt","r")

# a=input()
# b=input()
# sH=dict()
# for x in a:
#   sH[x]=sH.get(x, 0)+1
# for x in b:
#   sH[x]=sH.get(x, 0)-1
# if anagram-> increased key in for a will be deducted in for b loop
# for x in a:
#   if sH.get(x)>0:
#       print("NO")
#       break
# else:
#   print("YES")