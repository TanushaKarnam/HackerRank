students=[]
n=int(input())
for i in range(n):
    names=str(input())
    grades=float(input())
    lst=[names,grades]
    students.append(lst)
score=[]
name=[]
for grades in students:
    score.append(grades[-1])
sec_lowest=sorted(set(score))[1]
for names,grades in students:
    if grades==sec_lowest:
        name.append(names)
        name.sort()
print('\n'.join(name))
