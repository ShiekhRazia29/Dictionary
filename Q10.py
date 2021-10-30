#Find the number of values in the keys of the given dictionary
dict={
    'Alex':['subj1','subj2','subj3'],
    'David':['subj1','subj2']
}
count=0
for x in dict:
    if isinstance(dict[x], list):
     count += len(dict[x])
print(count)
 
