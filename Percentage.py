n=int(input("Number of students: "))
for i in range(n):
    name=str(input("Student name: "))
    marks=map(int,input("give three inputs: ").split())
    lst=[name,marks]
print(lst) 
