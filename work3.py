
#part A
#EX1

def make_rectangle(x,y,leghth,width):
    """create a rectangle"""
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
    """return length of rectangle"""
    return getitem_rectangle(r, 2)

def width(r):
    """return width of rectangle"""
    return getitem_rectangle(r, 3)

def diagonal(r):
    """return the len of diagonal of rectangle"""
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
    """change the edge len by factor"""
    return make_rectangle(x(r),y(r),length(r)*factor,width(r)*factor)

def average(number1,number2):
    """help func to calc a average of 2 elments"""
    return (number1+number2)/2

def average_rectangle(rect1,rect2):
    """calculte the average lengh of edges rectangle and middle it at location """
    middleX=(x(rect1)+x(rect2))/2
    middleY=(y(rect1)+y(rect2))/2
    avg_len=average(length(rect1),length(rect2))
    avg_wid=average(width(rect1),width(rect2))
    return make_rectangle(middleX,middleY,avg_len,avg_wid)


# # testing
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
#
# print_rectangle(average_rectangle(r3,r2))


# EX2
def make_vector(size, list):
    """craete a vector"""
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
    """print the vector"""
    return 'size = {0}; values = {1}'.format(vector(0), vector(1))


def value_at(vector, index):
    """return the value by index"""
    return vector(1)[index]


def reverse(vector):
    """return a new opposite vector"""
    return vector(1)[::-1]


def norm1(vector):
    """calculte the sum of absult of values in vector and return it"""
    index = 0
    sum = 0
    while index < vector(0):
        if vector(1)[index] < 0:
            vector(1)[index] = vector(1)[index] * -1
        sum = sum + vector(1)[index]
        index = index + 1
    return sum


def norm2(vector):
    """calculte the sqeroot of values in vector and return it"""
    from math import sqrt
    index = 0
    sum = 0
    while index < vector(0):
        sum = sum + (vector(1)[index] * vector(1)[index])
        index = index + 1
    return sqrt(sum)


def insert(vector, number):
    """add a new value to vector, return a new vector"""
    index = vector(0) + 1
    list1 = values(vector)
    new_list = list(list1)
    new_list.append(number)
    return make_vector(index, tuple(new_list))


def delete(vector, index):
    """erase a exsist value of vector, return a new vector"""
    new_size = vector(0) - 1
    list1 = values(vector)
    new_list = list(list1)
    del new_list[index]
    return make_vector(new_size, tuple(new_list))


def sort_vector(vector):
    """sorting the values from smaller to bigger"""
    list1 = values(vector)
    new_list = list(list1)
    new_list.sort()
    return make_vector(vector(0), tuple(new_list))


def add_vector(vector1, vector2):
    """return a new vector as result of sum vec1+vec2"""
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
    """return a new scalr as result of multy vec1*vec2"""
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

# ex2
def add_factors(courses, factors):
    '''The function returns the list of courses with updated scores after the factor'''
    after_factor = tuple(map(lambda index: (index[0], index[1] + factors[tuple
    (map(lambda index: index[0], factors)).index(index[0])][1])
    if index[0] in tuple(map(lambda index: index[0], factors)) else index, courses))
    return after_factor


# ex3
def total_average(courses, credits):
    '''The function returns the overall average of all courses'''
    from functools import reduce
    average_of_all = reduce(lambda first_grade, second_grade: first_grade + second_grade,
    (map(lambda first_grade: first_grade[1] * (credits[tuple(map(lambda first_grade: first_grade[0], credits)).index(first_grade[0])][1] /
    reduce(lambda first_grade, second_grade: first_grade + second_grade,
    map(lambda first_grade: first_grade[1], credits)))
    if first_grade[0] in tuple(map(lambda first_grade: first_grade[0], credits)) else first_grade, courses)))
    return average_of_all

# courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
# factors= (('c',15),('a',20))




# print(tuple(map(first_value_In_pair,courses)))
# print("avg",tuple(avg_grades(courses)))
# print(map(average1, courses))

#part C

# courses=(('a',80),('b',95),('c',75),('d',58))
# credit=(('a',2.5),('b',4),('c',3.5),('d',5))
# courses_dict=dict(courses)
# credit_dict=dict(credit)
#
# types={'t1':('a','b'),'t2':('c',),'t3':('d',)}

def make_warehouse(courseAVG,points_dict,list_course):
    """creating a warehouse to save data of grades"""
    def min_credits():
        """return the min credit points"""
        return courseAVG[min(points_dict)]

    def max_credit():
        """return the max credit points"""
        return courseAVG[max(points_dict)]

    def min_course(type_name):
        """search a minimum grade of spesific course type"""
        key1=list_course[type_name]
        temp_min =courseAVG[key1[0]]
        for i in key1:
            if(courseAVG[i]<temp_min):
                temp_min=courseAVG[i]
        return temp_min

    def max_course(type_name2):
        """search a maximum grade of spesific course type"""
        key2=list_course[type_name2]
        temp_max=courseAVG[key2[0]]
        for i in key2:
            if(courseAVG[i]>temp_max):
                temp_max=courseAVG[i]
        return temp_max

    def avg_course(type_name3):
        """calculate a average grade of spesific course type"""
        key3=list_course[type_name3]
        sum=0
        for i in key3:
           sum+=courses_dict[i]
        return sum/(len(key3))

    def add_course(new_course,new_grade,new_type):
        """add a new course just if it exsist in the warehouse"""
        if(new_type in list_course and new_course not in courseAVG.keys()):#check posible action
            temp_tuple=(list_course[new_type][0],new_course)#add a new key to dictionary of types
            list_course[new_type]=temp_tuple
            courseAVG[new_course]=new_grade#add a new grade to the match course
        else:
            print("Error the type don't exsist or the course is alreay belong to other type")

    return {'min_credits':min_credits,'max_credit':max_credit,'min_course':min_course,'max_course':max_course,'avg_course':avg_course,'add_course':add_course}

# w=make_warehouse(courses_dict,credit_dict,types)


# print(w['min_credits']())
# print(w['max_credit']())
# print(w['min_course']('t1'))
# print(w['max_course']('t1'))
# print(w['avg_course']('t1'))
# print("before",courses_dict,credit_dict,types)
# w['add_course']('e',90,'t2')
# print("after",courses_dict,credit_dict,types)
# print(w['max_course']('t2'))
# print(w['min_course']('t2'))
#
# print(w['avg_course']('t2'))

#ex5


def make_sequence(seq):
    """create a object and save the data"""
    seq=tuple(seq)
    def filter(func1=None):
        """filter the sequence according func1, return a tuple"""
        temp_seq=[]
        if func1==None:
            return seq
        for i in range(len(seq)):
            if func1(seq[i]):
                temp_seq.append(seq[i])
        return tuple(temp_seq)

    def filter_iterator(func2=None):
        """filter the sequence according func 2 a return a circle sequence, posible change index location by next or reverese"""
        tempiteartor=filter(func2)
        index=0

        def next():
            nonlocal index
            print(tempiteartor[index])
            index=(index+1)%len(tempiteartor)

        def reverse():
            nonlocal index
            index=(index-1)%len(tempiteartor)
            print(tempiteartor[index])

        return {'next':next,'reverse':reverse}

    def reverse():
        """return a opposite order of the sequence """
        end=len(seq)-1
        tempseq=list(seq)
        for j in range(len(seq)//2):
            tempseq[j],tempseq[end]=tempseq[end],tempseq[j]
            end-=1
        #print(tempseq)
        return tuple(tempseq)

    def extend(addition):
        """add a new sequence to exsist """
        nonlocal seq
        seq=seq+tuple(addition)

    return {'filter':filter,'filter_iterator':filter_iterator,'reverse':reverse,'extend':extend}

# s1=make_sequence((1,2,3,4,5))
# print(s1['filter'](lambda x:x%2==0))
#
# p1=s1['filter_iterator'](lambda x:x<4)
# p1['next']()
# p1['next']()
# p1['next']()
# p1['next']()
# p1['next']()
# p1['reverse']()
# p1['reverse']()
# p1['reverse']()
#
#
# s1['extend'](s1['filter'](lambda x:x%2!=0))
# print(s1['filter'](lambda x: x>2))
# print(s1['filter']())
#
# print((make_sequence(s1['reverse']()))['filter'](lambda x: x<4))
