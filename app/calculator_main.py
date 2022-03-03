from SCR. calculator import Calculator 
cal=Calculator()
x=10
y=12.5
print(x,'+',y,'=',cal.sum(x,y))
print(x,'-',y,'=',cal.substract(x,y))
print(x,'X',y,'=',cal.multiply(x,y))
print(x,'/',y,'=',cal.divide(x,y))
print(x,'/',y,'integer part is',cal.fdivide(x,y))
print(x,'/',y,'remainder is',cal.remainder(x,y))
x=10
y=0 
print(x,'/',y,'remainder is',cal.remainder(x,y))
