class calculator():
    def _init_ (self, a,b):
        self.a=a
        self,b=b
    def add(self1):
        return self.a+self.b
    def mul(self):
        return self.a*sefl.b
    def div(self):
        return self.a/self.b
    def sub (self):
        return self.a-self.b
a=int(input ("Enter first value:"))
b=int(input ("Enter first value:"))
obj=calculator (a,b)
choice=1
while choice!=0:
    print ("0. Exit")
    print ("1. Add")
    print ("2. Sub")
    print ("3. Multi")
    print ("4. Division")
choice = int ( input ( " Enter choice : " ) )
if choice == 1 :
    print ( " results : " , obj.add ( ) )
elif choice == 2 :
    print ( " results : " , obj.sub ( ) )
elif choice == 3 :
    print ( " results : " , obj.mul () )
    print ( " result : " , round ( obj.div ( ) , 2 ) )
elif choice == 4 :
    print ("exiting")
else:
    print ("invalid choice")
print()