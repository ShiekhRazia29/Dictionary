#To check whether a key exists in a dictiory or not
#For that we use a key word called "in"
key_word_exists={'name':"Razia",'Age':22,'Course':"Software Engineering",
'present':"Navgurkul Campus"}
if 'name' in key_word_exists:
    print("Yes the keyword name exists:",key_word_exists['name'])
else:
    print("No the keyword name doesnot exist in the dictionary")
#adding element to the dictionary
dic={'Name':"Razia",'age':22,'place':"Gulmarg"}
dic['organization']="NavGurkul"
dic['course']="Software Engineering"
print("dic",dic)