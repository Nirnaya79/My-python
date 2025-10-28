

work=[]
count=int(input("Enter range"))
for index in range(count):
    item=input("enter work:")
    work.append(item)

print("1. read")
print("2. write")
print("3. remove")
def read():
    print(work)
def delete():
    d=input("Enter task you want to delete:")
    work.remove(d)
    print(work)
choice=int(input("Enter choice:"))

if choice==1:
    read()

elif choice==2:
    count=int(input("How many task you want to enter?"))
    for i in range(count):
        task=input("Enter task:")
        work.append(task)

elif choice==3:
    delete()









