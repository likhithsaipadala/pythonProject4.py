import re
special_characters= "!@#$%^&*()}{|:<>?/.,;\][=-"
E=input("Enter your email:")
flag=0
for each in special_characters:
    if each==[0]:
        print("Invalid")
        flag=1
d=re.findall("^\d",E)
if d!=[]:
    print("Invalid")
    flag=1
a=re.findall('.+@\.[a-z]',E)
if a!=[]:
    print("Invalid")
    flag=1
if '@.' in E:
    print(Invalid)
    flag=1
if flag==0:
    l=re.findall(".+@.+\.[a-z].+",E)
    print(l)

P=input("Enter Password:")
rain=0
for eachs in special_characters:
    if eachs==[0]:
     print("Invalid Password")
     rain=0
q=re.findall("\d",P)
if q==[]:
    print("Invalid")
    rain=0
t=re.findall("[a-z]",P)
if t==[]:
    print("Invalid")
    rain=0
u=re.findall("[A-Z]",P)
if u==[]:
    print("Invalid")
    rain=0

if P>"5":
   print(P)

X=input("Login:")
if X!=l:
    print("Register for Login Credentials")
else:
    print("Valid")

Y=input("Enter Password:")
if Y!=P:
    print("Forget Password?")











