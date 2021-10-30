my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict:
    a.append(my_dict[i])
print(a)
a.sort()
w=0
t=[]
while len(a)<=2:
    t.append(a[i])
    w+=1
print(t)
# max=0
# b=[]
# x=0
# while x<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j+=1
#     x+=1
# # print(a)
# y=1
# while y<=3:
#     b.append(a[-y])
#     y+=1
# print(b)