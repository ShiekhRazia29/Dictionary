#creating a dictionary with two lists one contains keys and other contains values.
from typing import Iterator


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,6]
zip_Iterator=zip(list1,list2)
dict=dict(zip_Iterator)
print(dict)