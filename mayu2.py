name="mayank     "   
print(name.upper())
name="MAYANK"
print(name)
str1=name.lower()
print(str1)
name="MAYANK"
str1=name.swapcase()
print(str1)
name=" hello mayank how are you"
str1=name.title()
print(str1)
name="MAYANK"
print(name.isupper())
name="mayank"
str1=name.islower()
print(str1)
name="Hello Mayank How Are You"
str1=name.istitle()
print(str1)
name="7989jh355"
str1=name.isdigit()
print(str1)
name="mayank"
str1=name.isalpha()
print(str1)
name="5766jygtlil9"
str1=name.isalnum()
print(str1)
name=" "
print(name.isspace())
name="mayank"
str1=name.lstrip()
print(str1)
name="mayank     "
str1=name.rstrip()
print(str1)
name="    mayank    "
str1=name.strip()
print()
name="mayank"
old="may"
new="omg"
str1=name.replace(old,new)
print(str1)
name="hello-mayank-how-are-you"
str1=name.split("-")
print(str1)
name="mayank chauhan"
str1=name.split(" ")
print(str1)
name=('hello', 'mayank', 'how', 'are', 'you')
str1="-".join(name)
print(str1)
name="hi how are u"
print(name.startswith("hi"))
name="hi how are u"
print(name.endswith("u"))


for i in range(2):
    print("Mayank chauhan", i)
    for j in range(3):
        print("Thakur sahab", j)



a=0
b=1
n= int(input("enter no"))
for i in range(n):
    c=a+b;
    a=b;
    b=c;
print(c)

