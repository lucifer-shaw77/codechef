def rev(n):
    if len(n)==0:
        return n
    else:
        return rev(n[1:])+n[0]
n=input("enter your string: ")

print("reversed string is:",rev(n))
    
