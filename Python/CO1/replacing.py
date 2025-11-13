string_input=input("Enter the String: ")

first_char=string_input[0]
replaced=first_char + string_input[1:].replace(first_char,"$")
print(replaced)
