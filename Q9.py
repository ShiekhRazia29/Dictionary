string="missippii"
dic={}
for ch in string:
    occurs=string.count(ch)
    #print(ch,"Occurs",occurs)
    updated=dic.update({ch:occurs})
print(dic)
