dict={'a':[1,2,3,4],
       'b':["a","b","c"],
       'c':"nobody",
       'd':5,
       'e':('@',1,2,4)}
count=0
for k in dict:
    if isinstance(dict[k],int):
        count=count+1
    elif isinstance(dict[k],str):
        count +=1
    else:
        count += len(dict[k])
print("total length of the values is",count)
       