#5.2: Data Analysis with Numpy, Matplotlib, Scipy
#Numpy
print([1,2,3]*3)

"""
Revision
name = input("say your name: ")

if name == "David":
    print("welcome back " + name)
elif name == "David Emanuel":
    print("Hello master " + name)
else:
    print("you are not my master")
"""
print([i*3 for i in [1,2,3]])

#concatenate
[1,2,3]+[3,4,6]

#Sum two vector
a=[1,2,3]
b=[3,4,6]
print([a[i]+b[i] for i in range(len(a))])
#cross product or dot production
u = [1,2,3]
v = [4,5,6]

total = 0
for i in range(len(u)):
    total += u[i] * v[i] #soma os valores multiplicados entre eles [4,10,18] = 32
print(total)
