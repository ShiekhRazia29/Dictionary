dict={
    "first":1,
    "second":2,
    "third":1,
    "fourth":5,
    "five":5,"six":9,
    "seven":7
}
print("original dictionary will be as ",dict)
list1 =[] # create empty list
for val in dict.values(): 
  if val in list1: 
    continue 
  else:
    list1.append(val)

print(list1)