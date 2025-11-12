first =list(map(int,input("Enter the First List").split()))
second=list(map(int,input("Enter the Scond List").split()))

if len(first)==len(second):
    print("the Integers have same Length")
else:
    print("ith Dont have same lenth")

if sum(first)==sum(second):
    print("it have Equal Sum")
else:
    print("ItS Sum is not same at all")

common=set(first)&set(second)

if common:
    print("Common values are:",common)
else:
    print("There is no Common Values")
