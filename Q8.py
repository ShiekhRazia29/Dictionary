name={}
for i in range(10):
    name_student=input("Enter the name:")
    serial_no=int(input("Enter serial number:"))
    name.update({name_student:serial_no})
print(name)