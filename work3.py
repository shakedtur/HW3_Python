
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
    """help func to calc a average of 2 elments"""
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
#
# print_rectangle(average_rectangle(r3,r2))


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

courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
factors= (('c',15),('a',20))


# print(tuple(map(first_value_In_pair,courses)))
# print("avg",tuple(avg_grades(courses)))
# print(map(average1, courses))


#ex2

#need to fixxxxxxxxxxx!!!!!!!!!!!!!!!!!!!

def add_factors(couse_seq,factor_seq):
    """func to add a points to a course by factor paramerter"""
    avg_courses=tuple(avg_grades(couse_seq))
    name_ofCours=tuple(map(first_value_In_pair,factor_seq))
    for name_ofCours in avg_courses:
        print(name_ofCours)

#add_factors(courses,factors)


#part C

# courses=(('a',80),('b',95),('c',75),('d',58))
# credit=(('a',2.5),('b',4),('c',3.5),('d',5))
# courses_dict=dict(courses)
# credit_dict=dict(credit)
#
# types={'t1':('a','b'),'t2':('c',),'t3':('d',)}

def make_warehouse(courseAVG,points_dict,list_course):

    def min_credits():
        return courseAVG[min(points_dict)]

    def max_credit():
        return courseAVG[max(points_dict)]

    def min_course(type_name):
        key1=list_course[type_name]
        temp_min =courseAVG[key1[0]]
        for i in key1:
            if(courseAVG[i]<temp_min):
                temp_min=courseAVG[i]
        return temp_min

    def max_course(type_name2):
        key2=list_course[type_name2]
        temp_max=courseAVG[key2[0]]
        for i in key2:
            if(courseAVG[i]>temp_max):
                temp_max=courseAVG[i]
        return temp_max

    def avg_course(type_name3):
        key3=list_course[type_name3]
        sum=0
        for i in key3:
           sum+=courses_dict[i]
        return sum/(len(key3))

    def add_course(new_course,new_grade,new_type):
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