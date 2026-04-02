print("--------------------HELLO WORLD------------------------")
name ="jacy"
print(name)
print("ADDITION:2+3=",2+3)
print("SUBTRACT:5-2",5-2)
print("MULTIPLICATION:4*3",4*3)
print("DIVISION:10/2",10/2)
print("MODULUS:10%3",10%3)
n=4
print(n)
print("SQUARE:")
print(n*n)
print("CUBE:",n**3)
print("------swap--------")
a,b=1,2
a,b=b,a
print(a,b)
print("EVEN" if n%2==0 else "ODD")
print("positive" if n>0 else "negative")
print(max(3,7))
print(min(3,7))
print(sum([1,2,3]))
print(len("abc"))
print("abc".upper())
print("ABC".lower())
print("abc"[::-1])
s="madam"
print(s==s[::-1])
for i in range(1,6):print(i)
print([i for i in range(1,11) if i%2])
f=1
for i in range(1,6):f*=i
print(f)
a,b=0,1
for a in range(5):
    print(a,end=" ")
    a,b=b,a+b
n=7
print(all(n%i for i in range(2,n)))
