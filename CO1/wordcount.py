string = input ("Enter rthe String")
words = string.split()
word_count={}
for i in words:
    i =i.lower()
    if i in word_count:
        word_count[i] +=1
    else:
        word_count[i] =1

print(word_count)
