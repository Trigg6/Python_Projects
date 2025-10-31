string_input=input("enter the String: ")
first_char=string_input[0]
last_char=string_input[-1]

changed=last_char + string_input[1: -1] + first_char
print(changed)
