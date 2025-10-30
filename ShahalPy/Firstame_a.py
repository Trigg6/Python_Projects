names_input=input("Enetr the Full anmes With Commas")
names = [ for name in names_input.split(",")]


first_names=[]
for name in names:
     first_names.append(name.split()[0])
     
print(first_names)

count=0
for i in first_names:
     count+=name.count("a")
print(count)
