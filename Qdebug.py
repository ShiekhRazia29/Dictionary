#guess output from the given snippet
#1
#a={(1,2):1,(2,3):2}
#print(a[1,2]) 
#2
#a={'a':1,'b':2,'c':3}
#print(a['a','b'])
#3
fruit={}
def addone(index):
    if index in fruit:
        fruit[index] +=1
    else:
        fruit[index]=1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')
print(len(fruit))
print(fruit)
#Q4
student={}
age={}
details={}
student['name']='bikki'
age['student_age']=14
details['age']=age
print(len(details['age']))#student at place of age gives key error
#Q5
my_dict={}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12
sum=0
for k in my_dict:
    sum+=my_dict[k]
print(sum)
print(my_dict)
#Q6
#box={}
#jars={}
#crates={}
#box['biscuit']=1
#box['cake']=3
#jars['jam']=4
#crates['jars']=jars
#print(len(crates[box])) #dict is not hashable
#Q7
rec={
    'Name':'Python',
    'Age':'20',
    'Addr':'NJ',
    'country':'USA'
}
id1=id(rec)
del rec
rec={  'Name':'Python',
    'Age':'20',
    'Addr':'NJ',
    'country':'USA'
}
id2=id(rec)
print(id1==id2)