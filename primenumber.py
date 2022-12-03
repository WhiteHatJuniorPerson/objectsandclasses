

class Primenumber:
    def __init__(self,number):
        self.number=number
    
    def primenumber(self):
        factors=0
        for i in range(1,self.number+1):
            if self.number%i==0:
                factors=factors+1
        if factors==2:
            print('this number is a prime number')
        else:
            print('this number is not a prime number')

p = Primenumber(18)
p.primenumber()