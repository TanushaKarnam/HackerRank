import textwrap
def wrap(string,max_width):
    a=textwrap.wrap(string, width=max_width)
    return "\n".join(a)
    return

string=input("enter the string: ")
max_width=int(input("enter the width: "))
result= wrap(string,max_width)
print(result)