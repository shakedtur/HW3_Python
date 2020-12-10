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

def average_rectangle(rect1,rect2):
    middleX=(x(rect1)+x(rect2))/2
    middleY=(y(rect1)+y(rect2))/2
    avg_len=average(length(rect1),length(rect2))
    avg_wid=average(width(rect1),width(rect2))
    return make_rectangle(middleX,middleY,avg_len,avg_wid)


#testing
# r1=make_rectangle(3,4,10,26)
# print(x(r1))
# print(diagonal(r1))
# print(print_rectangle(r1))
# print(center(r1))
# print(distance(r1,make_rectangle(6,9,5,8)))
# print(print_rectangle(move(r1,2,-3)))
# print(print_rectangle(resize(r1,0.5)))
# r2=make_rectangle(6,9,5,8)
# r3=make_rectangle(3,4,10,26)
# print_rectangle(r3)
# print_rectangle(r2)
# print_rectangle(average_rectangle(r3,r2))

#EX2
def make_vector(size, list):
    def dispatch(index):
        if index == 0:
            return size
        elif index == 1:
            return list
        else:
            return "error"
    return dispatch


def size(vector):
    return vector(0)


def values(vector):
    return vector(1)


def print_vector(vector):
    return 'size = {0}; values = {1}'.format(vector(0), vector(1))


def value_at(vector, index):
    return vector(1)[index]


def reverse(vector):
    return vector(1)[::-1]


def norm1(vector):
    index = 0
    sum = 0
    while index < vector(0):
        if vector(1)[index] < 0:
            vector(1)[index] = vector(1)[index] * -1
        sum = sum + vector(1)[index]
        index = index + 1
    return sum


def norm2(vector):
    from math import sqrt
    index = 0
    sum = 0
    while index < vector(0):
        sum = sum + (vector(1)[index] * vector(1)[index])
        index = index + 1
    return sqrt(sum)


def insert(vector, number):
    index = vector(0) + 1
    list1 = values(vector)
    new_list = list(list1)
    new_list.append(number)
    return make_vector(index, tuple(new_list))


def delete(vector, index):
    new_size = vector(0) - 1
    list1 = values(vector)
    new_list = list(list1)
    del new_list[index]
    return make_vector(new_size, tuple(new_list))


def sort_vector(vector):
    list1 = values(vector)
    new_list = list(list1)
    new_list.sort()
    return make_vector(vector(0), tuple(new_list))


def add_vector(vector1, vector2):
    list1 = values(vector1)
    list2 = values(vector2)
    new_list1 = list(list1)
    new_list2 = list(list2)
    list3 = []
    if len(new_list1) >= len(new_list2):
        temp_len = vector1(0)
    else:
        temp_len = vector2(0)
    for i in range(temp_len):
        list3.append(new_list1[i] + new_list2[i])
    return make_vector(temp_len, tuple(list3))


def mult_scalar(vector1, vector2):
    list1 = values(vector1)
    list2 = values(vector2)
    new_list1 = list(list1)
    new_list2 = list(list2)
    list3 = []
    if len(new_list1) >= len(new_list2):
        temp_len = vector1(0)
    else:
        temp_len = vector2(0)
    for i in range(temp_len):
        list3.append(new_list1[i] * new_list2[i])
    return make_vector(temp_len, tuple(list3))


#testing
# v1 = make_vector(5, (1, 2, 3, 4, 5))
# print(v1)
# print(size(v1))
# print(values(v1))
# print(print_vector(v1))
# print(value_at(v1, 3))
# print(reverse(v1))
# print(norm1(v1))
# print(norm2(v1))
# print(print_vector(insert(v1, 6)))
# print(print_vector(delete(v1, 2)))
# v3 = delete(delete(delete(v1, 0), 3), 1)
# print(print_vector(v3))
# v2 = make_vector(5, (1, 8, 3, 9, 5))
# print(print_vector(sort_vector(v2)))
# print(print_vector(mult_scalar(v1, v2)))


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
