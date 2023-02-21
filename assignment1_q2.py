print("Reverse Program/ reverse word")
word="Edyoda"
for i in range(len(word)-1, -1, -1):
    print(word[i], end='')
    
    
print("------OR------")


word="edyoda"
reverse = ''
for i in word:
    reverse=i+reverse
print(reverse)
    