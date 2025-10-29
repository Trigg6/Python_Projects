print("Leap Years")
endyear = int(input("Enter the Last Year"))
print(f"\n Leap Years From 2025 to {endyear} are: ")
for year in range (2025 ,endyear+1 ):
    if(year %4==0 and year %100!=0) or (year % 400==0):
        print(year)
