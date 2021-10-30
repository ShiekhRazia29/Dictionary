init_dic={'a':1,'b':2,'c':1,'d':3,'e':2,'f':4}
print("Initial dictionary ",str(init_dic))
rev_dic={}
for k ,v in init_dic.items():
    rev_dic.setdefault(v,set()).add(k)
    result=[k for k,v in rev_dic.items()    if len(v)>1 ]
print("duplicate values",str(result))
 