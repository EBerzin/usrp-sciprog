
word = ''
sentence = ''

while word not in ["?", ".", "!"]:
    word = input("Enter a word (. ! or ? to end): ")
    sentence = sentence + word + " "

print(sentence)