#print three largest numbers from a dictionary
from heapq import nlargest
my_dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
three_largest=nlargest(3,my_dict,key=my_dict.get)
print(three_largest)