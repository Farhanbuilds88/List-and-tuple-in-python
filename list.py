marks=[12.3,23,24.35]
print(marks);
print(type(marks));
print(marks[0])

print(len(marks))
# we can store multiple data types in single list
students=["karan",87.9,"delhi"]
print(students)
#strings are immutable and list are mutable in python
students[1]=13;
print(students[1]);
#slicing in list
mark=[12,34,5,6,7]
print(mark[0:3])
print(mark[-3:-5])

#list methods
list =[2 ,1,4];
#append adding new element to the start of the list  mutation
list.append(6);
print(list);

#second method is sorting 
list.sort();
print(list);
list.sort(reverse=True);
print(list);

# list.sort(reverse=true for descending order)
fruits=["farhan","amir","zain","muxammil"];
fruits.sort();
print(fruits);
fruits.sort(reverse=True);
print(fruits)
#reverse method 
teachers=["arif","farhan","moiz","muzammil","ayzaz"]
teachers.reverse();
print(teachers)

points=[34,45,56,"girl","cake","50"]
points.reverse();
print(points);

alphabet=['r','t','u','e','w','a']
alphabet.reverse();
print(alphabet);

#insert method in particular index we are inserting the value 
players=["messi","ronaldo","salah","neymar","silva"]
players.insert(2,"halland")
print(players)

# remove method deletes a value
players.remove("messi");
print(players);

players.pop(4);
print(players)
