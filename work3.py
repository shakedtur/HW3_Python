
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
    """printing the rectangle as point=(x,y) ; size= lenXwid"""
    return 'Rectangle: point=({0},{1}); size= {2}X{3}'.format(x(r),y(r),length(r),width(r))

def center(r):
    """calc the center point of the rectangle"""
    return (x(r)+length(r)/2,(y(r)+width(r)+y(r))/2)

def distance(r1,r2):
    """calculate the distance between 2 center of 2 retangles"""
    from math import sqrt
    subX=(center(r1)[0]-center(r2)[0])**2
    subY=(center(r1)[1]-center(r2)[1])**2
    return sqrt(subX+subY)

def move(r,deltaX,deltaY):
    """create a new rectangle and move it according deltaX ,deltaY"""
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

#ex1
def make_pair(x,y):
    """func to crate a pair """
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

# def add(a,b):
#     """func sum of 2 values"""
#     return a+b

def average1(list_of_values):
    """calculate average of list"""
    return sum(list_of_values)/len(list_of_values)

def merage(one,two):
    """return to valus as a sequence"""
    return one,two

def avg_grades(sequence1):
    """function to calculate average grades by courses name and merage them"""
    avg=(map(average1, map(secend_value_In_pair, sequence1)))#split the courses grades to other list and calc the averge
    seq2=(map(first_value_In_pair,courses))#split the courses names
    return map(merage,seq2,avg)#merage the match data to pair


def first_value_In_pair(pairs):
    return pairs[0]

def secend_value_In_pair(pairs):
    return pairs[1]

courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
factors= (('c',15),('a',20))


print(tuple(map(first_value_In_pair,courses)))
print("avg",tuple(avg_grades(courses)))
print(map(average1, courses))


#ex2

def add_factors(seq1,seq2):
    pass





