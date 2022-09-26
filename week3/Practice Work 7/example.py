#example 1
def printChar (s):
    print (s)
sim = input ('Enter Simbol')
printChar (sim)
printChar('*')
#example 2
x=3 # global variable
def pr(): #procedure without 
    print(x)#parametrs 
    
x=3
print (x)
def pr():
    global x
    x=pow(x, 10)
    print(x)
pr()
# example 3 Functions 
def sumD(n):
    summa = 0
    while n!= 0:
        summa += n % 10
        n=n//10
    return summa
print (sumD (int(input())))