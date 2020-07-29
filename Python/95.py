import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        a = self.real+no.real
        b = self.imaginary+no.imaginary
        if a<0 and b<0:
            return ("-%.2f-%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b<0:
            return ("%.2f-%.2fi"%(abs(a),abs(b)))
        elif a<0 and b>=0:
            return ("-%.2f+%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b>=0:
            return ("%.2f+%.2fi"%(abs(a),abs(b)))
    def __sub__(self, no):
        a = self.real-no.real
        b = self.imaginary-no.imaginary
        if a<0 and b<0:
            return ("-%.2f-%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b<0:
            return ("%.2f-%.2fi"%(abs(a),abs(b)))
        elif a<0 and b>=0:
            return ("-%.2f+%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b>=0:
            return ("%.2f+%.2fi"%(abs(a),abs(b)))
    
    def __mul__(self, no):
        a=self.real*no.real-self.imaginary*no.imaginary
        b=no.imaginary*self.real+self.imaginary*no.real
        if a<0 and b<0:
            return ("-%.2f-%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b<0:
            return ("%.2f-%.2fi"%(abs(a),abs(b)))
        elif a<0 and b>=0:
            return ("-%.2f+%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b>=0:
            return ("%.2f+%.2fi"%(abs(a),abs(b)))
    def __truediv__(self, no):
        x = no.real**2+no.imaginary**2
        a = (self.real*no.real+self.imaginary*no.imaginary)/x
        b = (-no.imaginary*self.real+self.imaginary*no.real)/x
        if a<0 and b<0:
            return ("-%.2f-%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b<0:
            return ("%.2f-%.2fi"%(abs(a),abs(b)))
        elif a<0 and b>=0:
            return ("-%.2f+%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b>=0:
            return ("%.2f+%.2fi"%(abs(a),abs(b)))
        
    def mod(self):
        a = pow(self.real**2+self.imaginary**2, 0.5)
        b = 0
        if a<0 and b<0:
            return ("-%.2f-%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b<0:
            return ("%.2f-%.2fi"%(abs(a),abs(b)))
        elif a<0 and b>=0:
            return ("-%.2f+%.2fi"%(abs(a),abs(b)))
        elif a>=0 and b>=0:
            return ("%.2f+%.2fi"%(abs(a),abs(b)))

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')