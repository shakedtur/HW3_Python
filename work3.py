
#part A
#EX1

def make_rectangle(x,y,leghth,width):
    def dispatch(index):
        if index==0:
            return x
        elif index==1:
            return y
        elif index==2:
            return leghth
        elif index==3:
            return width
        else:
            return "error"
    return dispatch

def getitem_rectangle(r, i):
    return r(i)

def x(r):
    return getitem_rectangle(r, 0)

def y(r):
    return getitem_rectangle(r, 1)

def length(r):
    return getitem_rectangle(r, 2)

def width(r):
    return getitem_rectangle(r, 3)

def diagonal(r):
    from math import sqrt
    return sqrt(length(r)**2+width(r)**2)

def print_rectangle(r):
    return 'Rectangle: point=({0},{1}); size= {2}X{3}'.format(x(r),y(r),length(r),width(r))

def center(r):
    return (x(r)+length(r)/2,(y(r)+width(r)+y(r))/2)

def distance(r1,r2):
    from math import sqrt
    subX=(center(r1)[0]-center(r2)[0])**2
    subY=(center(r1)[1]-center(r2)[1])**2
    return sqrt(subX+subY)

def move(r,deltaX,deltaY):
    return make_rectangle(x(r)+deltaX,y(r)+deltaY,length(r),width(r))

def resize(r,factor):
    return make_rectangle(x(r),y(r),length(r)*factor,width(r)*factor)

def average(number1,number2):
    return (number1+number2)/2

r1=make_rectangle(3,4,10,26)
print(x(r1))
print(diagonal(r1))
print(print_rectangle(r1))
print(center(r1))
print(distance(r1,make_rectangle(6,9,5,8)))
print(print_rectangle(move(r1,2,-3)))
print(print_rectangle(resize(r1,0.5)))



#part B

def make_pair(x,y):
    def dispatch1(i):
        if i==0:
            return p[0]
        elif i==1:
            return p[1]
        else:
            return "error"
    return dispatch1

def get_item_pair(p,i):
    return p(i)

from functools import reduce

def add(a,b):
    return a+b

def avgrage1(list_of_values):
    return sum(list_of_values)/len(list_of_values)

def merage(one,two):
    return (one,two)
#need fix
def avg_grades(sequence1):
    avg=tuple(map(avgrage1, map(secend_value_In_pair, sequence1)))
    seq2=tuple(map(first_value_In_pair,courses))
    from functools import reduce
    return reduce(merage,avg)

def first_value_In_pair(pairs):
    return pairs[0]
def secend_value_In_pair(pairs):
    return pairs[1]

reshima=[10,5,3]
print(avgrage1(reshima))


courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])

print(tuple(map(first_value_In_pair,courses)))
print(avg_grades(courses))
print(map(avgrage1,courses))

