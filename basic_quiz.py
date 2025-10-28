print("Enter your todays to-do list:")
to_do_list=[]
num=int(input("Enter the number of tasks:"))

for task in range(num):
    t=input("Enter the task:")
    to_do_list.append(t)

def view(to_do_list):
    print(to_do_list)

def add(to_do_list):
    a = input("Enter the task:")
    to_do_list.append(a)

def remove(to_do_list):
    r=input("Enter the task to be removed:")
    to_do_list.remove(r)
    print("Removed successfully:")

print("Enter a process:")
print("1)view \n 2)add \n 3)remove ")
process=int(input())
if process== 1:
    view(to_do_list)
elif process==2:
    add(to_do_list)

elif process==3:
    remove(to_do_list)
else:
    print("Invalid")





