# tuples are also immutable means we can not make changes to them like the strings
tup=(1,2,3,4,5)
print(type(tup))
print(tup[3]);
#tup[0]=45 this is not allowed in tuple
footballers=("messi",)
print(type(footballers))
tup.index(3)
print(tup.index(3));
print(tup.count(3));

a=input("enter name of movie one:")
print(a)
b=input("enter the name movie two ")
print(b)
c=input("enter the name of the movie three")
print(c)

movies=[]
movies.append(a)
movies.append(b)
movies.append(c)

print(movies)