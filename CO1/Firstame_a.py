names_1=input("Enter the Full anmes With Commas")

names_input=[]
names_input=names_1.split(",")
  

first_names=[]
for name in names_input:
     first_names.append(name.split()[0])
     
print(first_names)

count=0
for i in first_names:
     count+= i.count('a')
print(count)
