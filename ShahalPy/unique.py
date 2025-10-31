colours_input1=input("Enetr the Colours Separated by Comma")
colour1=colours_input1.split(',')

colours_input2=input("Enetr the Colours Separated by Commas")
colour2=colours_input2.split(',')
unique = [color for color in colour1 if color not in colour2]
print(unique)
