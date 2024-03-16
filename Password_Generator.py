import string
import random
l=int(input("Enter length of the password you want to generate:"))
a= string.ascii_lowercase
b=string.ascii_uppercase
c=string.digits
d="!@#$%^&*?/"
p=[]
p.extend(list(a))
p.extend(list(b))
p.extend(list(c))
p.extend(list(d))
random.shuffle(p)
print("".join(p[0:l]))
