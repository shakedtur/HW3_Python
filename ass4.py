### Q2 - Q6 ###: see solutions of past exams

### Q9 - Q10 ###: see solutions of past exams

### Q7 - Q8 ###:
from math import atan2, sin, cos, pi,gcd
class ComplexRI(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)
##    def __str__(self):
##        return 'complex number in cartezian representaion: {0} + i*{1}'.format(self.real, self.imag)
    

class ComplexMA(object):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)

def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)

def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)

print(add_complex(ComplexRI(1, 2), ComplexMA(2, pi/2)))
print(mul_complex(ComplexRI(0, 1), ComplexRI(0, 1)))
##ComplexRI(1.0000000000000002, 4.0)
##ComplexMA(1.0, 3.141592653589793)

ComplexRI.__add__ = lambda self, other: add_complex(self,other)									
ComplexMA.__add__ = lambda self, other: add_complex(self,other) 									
ComplexRI.__mul__ = lambda self, other: mul_complex(self,other) 									
ComplexMA.__mul__ = lambda self, other: mul_complex(self,other)

print(ComplexRI(1, 2) + ComplexMA(2, 0))
print(ComplexRI(0, 1) * ComplexRI(0, 1))
##ComplexRI(3.0, 2.0)
##ComplexMA(1.0, 3.141592653589793)


class Rational(object):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)

def iscomplex(z):
    return type(z) in (ComplexRI, ComplexMA)

def isrational(z):
    return type(z) == Rational

def add_complex_and_rational(z, r):
    return ComplexRI(z.real + r.numer/r.denom, z.imag)

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat'}

def add(z1, z2):
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)

add.implementations = {}
add.implementations[('com', 'com')] = add_complex
add.implementations[('com', 'rat')] = add_complex_and_rational
add.implementations[('rat', 'com')] = lambda x, y: add_complex_and_rational(y, x)
add.implementations[('rat', 'rat')] = add_rational

print(add(ComplexRI(1.5, 0), Rational(3, 2)))
print(add(Rational(5, 3), Rational(1, 2)))
##ComplexRI(3.0, 0)
##Rational(13, 6)

def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)

def mul_complex_and_rational(z, r):
    return ComplexMA(z.magnitude * r.numer / r.denom, z.angle)

mul_rational_and_complex = lambda r, z: mul_complex_and_rational(z, r)
apply.implementations = {('mul', ('com', 'com')): mul_complex,
			('mul', ('com', 'rat')): mul_complex_and_rational,
			('mul', ('rat', 'com')): mul_rational_and_complex,
			('mul', ('rat', 'rat')): mul_rational}
adders = add.implementations.items()
apply.implementations.update({('add', tags):fn for (tags, fn) in adders})

print(apply('add', ComplexRI(1.5, 0), Rational(3, 2)))
##ComplexRI(3.0, 0)
print(apply('mul', Rational(1, 2), ComplexMA(10, 1)))
##ComplexMA(5.0, 1)

class Exponential():
    def __init__(self, base, power):
        self.base = base
        self.power = power

    def __repr__(self):
        return 'Exponential({0},{1})'.format(self.base, self.power)

type_tag.tags[Exponential] = 'exp'

def mul_exponential_and_complex(e, c):
    return ComplexMA(e.base*pow(10,e.power)*c.magnitude, c.angle)

apply.implementations[('mul',('exp','com'))] = mul_exponential_and_complex
apply.implementations[('mul',('com','exp'))] = lambda x,y: mul_exponential_and_complex(y,x)

print(apply('mul', Exponential(2,-4), ComplexMA(10,1)))
##ComplexMA(0.002, 1)
print(apply('mul', Exponential(2,-4), ComplexRI(3,4)))
##ComplexMA(0.001, 0.9272952180016122)

def rational_to_complex(x):
    return ComplexRI(x.numer/x.denom, 0)
def exponential_to_complex(x):
    return ComplexRI(x.base*pow(10, x.power), 0)

coercions = {('rat', 'com'): rational_to_complex}
coercions[('exp','com')] = exponential_to_complex

def coerce_apply(operator_name, x, y):
    tx, ty = type_tag(x), type_tag(y)
    if tx != 'com':
        if (tx, 'com') in coercions:
            tx, x = 'com', coercions[(tx, 'com')](x)
        else:
            return 'No coercion possible!'
    if ty != 'com':
        if (ty, 'com') in coercions:
            ty, y = 'com', coercions[(ty, 'com')](y)
        else:
            return 'No coercion possible!'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)

coerce_apply.implementations = {('mul', 'com'):mul_complex,
				('add', 'com'): add_complex}

print(coerce_apply('add', ComplexRI(1.5, 0), Rational(3, 2)))
##ComplexRI(3.0, 0)
print(coerce_apply('mul', Rational(1, 2), ComplexMA(10, 1)))
##ComplexMA(5.0, 1.0)
print(coerce_apply('mul', Exponential(2,-4), Rational(1,3)))
##ComplexMA(6.666666666666667e-05, 0.0)
print(coerce_apply('mul', Exponential(2,-4), Exponential(3,-5)))
##ComplexMA(6.000000000000001e-09, 0.0)









