#largest number in the dictionary
from heapq import nlargest
my_dict={'a':400,'b':300,'c':200,'d':560,'e':900}
Three_largest=nlargest(3,my_dict.values()) #(,key=my_dict.get) is used to get keys with largest values 
print(Three_largest) 