dic={
    'ball':"red",
    'bat':4,
    'wicket':8,
    'ball':'green',
    "bat":3
}
#dic2={}
#for k,v in dic.items():
#    dic2[k]=v
#print(dic2)
print(dic) # removes all the duplicates as the dictionaries doesnt contain duplicate values
result={}
for key,value in dic.items():
    if value not in result.values():
        result[key]=value
print(result)