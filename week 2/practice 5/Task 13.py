text = input("Write any text in parenthesis for example (I love Python)") 
print(text[text.find('(') + 1:text.find(')')])
