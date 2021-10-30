#sorting the values in ascending order
my_dict={'sabrina':57,'Aabir':40,'Jabeena':54,'Razia':45,'Ishita':55,"jayshri":66}
sort_order=sorted(my_dict.items(),key=lambda x:x[1],reverse=True) #gives in decending order True can be replaced with 
for i in sort_order:                                               #false to covert in ascending order
    print(i[0],":",i[1])