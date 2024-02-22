
def count_string(string,sub_string):
    c=0
    for i in range(0,len(string)):
        t=string[i:]
        if t.startswith(sub_string):
            c+=1
    return c    
string=input("Enter the main string: ").strip()
sub_string=input("Enter the sub string: ").strip()
count=count_string(string,sub_string)
print(count)