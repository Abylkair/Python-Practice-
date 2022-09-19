text = "amazing and croci it's example" #text 
 
for w in text.split(): # go through every word
    if(w.startswith("a") or w.endswith("i")): # If the word begins with the letter a, or ends with i
        print(w) 