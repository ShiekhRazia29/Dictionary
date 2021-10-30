# #Q1.Unique values from the list of dictionaries
# dict= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# unique_values=list(set(val for dic in dict for val in dic.values()))
# print(str(unique_values))




# #Q2 draw pattern of diamond shape
# n = 7
# for a1 in range(1, (n+1)//2 + 1): 
#     for a2 in range((n+1)//2 - a1):
#         print(" ", end = "")
#     for a3 in range((a1*2)-1):
#         print("*", end = "")
#     print()

# # for a1 in range((n+1)//2 + 1, n + 1): 
# #     for a2 in range(a1 - (n+1)//2):
# #         print(" ", end = "")
# #     for a3 in range((n+1 - a1)*2 - 1):
# #         print("*", end = "")
# #     print()



# #Q3 sort odd and keep even unchanged
# # a=[2,4,3,1,9,6,5,7]
# # a2=[]
# # for x in a:
# #     if x%2==0:
# #         a2.append(x)
# #     else:
# #         a.sort()
# #         a2.append(x)
# # print(a2)


# # BRACES = { '(': ')', '[': ']', '{': '}' }
# # def group_check(s):
# #     stack = []
# #     for b in s:
# #         c = BRACES.get(b)
# #         if c:
# #             stack.append(c)
# #         elif not stack or stack.pop() != b:
# #             return False
# # #     return not stack
# # password=input("Enter a password:")
# # islower="abcdefghijklmnopqrstuvwxyz"
# # isupper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # integers=1234567890
# # special='@#$%^&*()!'
# # if len(password)>=6:
# #     if password in(islower,isupper,integers,special):
# #         print("Strong password")
# #     else:
# #         print("Weak password")
# # else:
#     #print("Length should be 6 or more than that")


# i = input("Enter a string:")
 
# s = []
# for c in i:
#     if not s:
#         s.append(c)
#     else:
#         if s[-1] == c:
#             s.pop()
#         else:
#             s.append(c)
             
# if not s:
#     print("Empty String")
# else:
#     print (''.join(s))

#strong password hacker rank
import math
import os
import random
import sys
import re
def minimumNumber(n,password):
    spl_char="!@#$%^&*()-+"
    l=[0,0,0,0]
    for char in password:
        if char.isdigit():
            l[0]=1
        elif char.islower:
            l[1]=1
        elif char.isupper:
            l[2]=1
        elif char in spl_char:
            l[3]=1
    return max(6-len(password),4-sum(l))
#Breaking the records
  mincount=maxcount=0
    minscore=maxscore=scores[0]
    for i in range(1,len(scores)):
        if minscore<scores[i]:
            minscore=scores[i]
            mincount+=1
        elif maxscore>scores[i]:
            maxscore=scores[i]
            maxcount+=1
    return mincount,maxcount
#string construction
return len(set(s))
#Games of thrones
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    s=Counter(s)
    total=0
    for key,val in s.items():
        total+=val%2
    if total>1:
        return "NO"
    else:
        return "YES"
#pangrams
 t=set(s.lower())-set(' ')
    if len(t)==26:
        return "pangram"
    else:
        return "not pangram"
#beautiful movies
    count=0
    for x in range(i,j+1):
        rev=int(str(x)[::-1])
        if abs(x-rev)%k==0:
            count+=1
    return count
#Drawig book
 front=p//2
    if n%2==1:
        back=(n-p)//2
    else:
        back=(n-p+1)//2
    return min(front,back)
#superReduced string
 result=[]
    for i in range(len(s)):
        if len(result)==0 or result[-1]!=s[i]:
            result.append(s[i])
        else:
            result.pop()
    if len(result)==0:
        return "Empty String"
    else:
        return "".join(result) 