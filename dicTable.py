dict={}
dict1={1:['Razia',22,'Software','Badgam'],
2:['Sabrina',20,'Software','Kupwara'],
3:['Ariya',18,'Mechanical','Bandipora']}
print("{:<10} {:<10} {:<10} {:10}".format('Name','Age','Course','Place'))
for key,value in dict1.items():
    name,age,course,place=value
    print("{:<10} {:<10} {:<10} {:10}".format(name,age,course,place))