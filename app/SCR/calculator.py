class Calculator():
    def sum(self,x,y):
        return x+y
    def substract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y==0:
            return 'Error! The dividing number can NOT be zero'
        return x/y
    def fdivide(self,x,y):
        if y==0:
            return 'Error! The dividing number can NOT be zero'
        return x//y
    def remainder(self,x,y):
        if y==0:
            return 'Error! The dividing number can NOT be zero'
        return x%y
if __name__=='__main__':
    cal=Calculator()
    print(cal.multiply(15,12.5))
    print(cal.remainder(15,0))
 
