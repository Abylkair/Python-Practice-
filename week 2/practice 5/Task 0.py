#Task 0
def Palidromornot(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
phrase = input ("Write word to check Is Palindrome or not:")
s = (phrase) 
ans = Palidromornot(s)
 
if (ans):
    print("True")
else:
    print("False")



