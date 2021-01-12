

#part 1

#a
class Date:
    import datetime
    current=datetime.datetime.now()
    def __init__(self,d=current.day,m=current.month,y=current.year):
        from datetime import datetime
        self.day= d if 0<d<=31 else datetime.now().day
        self.month= m if 0<m<=12 else datetime.now().month
        self.year= y if 1900<y else datetime.now().year

    def __str__(self):
        return '%02d/%02d/%02d' % (self.day, self.month, self.year)

    def PrintDate(self):
        print("{0}/{1}/{2}".format(self.day,self.month,self.year))

#b
class Temperature(Date):
    from datetime import datetime
    current1 = datetime.now()
    def __init__(self,t,d=current1.day,m=current1.month,y=current1.year):
        Date.__init__(self,d,m,y)
        self.temperature=t

    def __str__(self):
        if(self.temperature>0):
            return "+%d C: %02d/%02d/%02d"%(self.temperature,self.day,self.month,self.year)
        else:
            return "%d C: %02d/%02d/%02d" % (self.temperature, self.day, self.month, self.year)

    def __add__(self,other):
        return self.temperature+other.get_Tempeature()

    def get_Tempeature(self):
        return self.temperature

    def compareTemp(self, other):
       if self.get_Tempeature()> other.get_Tempeature():
           return self
       else:
           return other

#c
class Location():

    def __init__(self,city,func1=None):
        super()
        self.place_name=city
        self.temp_list=[]

    def printLocation(self):
        print(self.place_name)
        if(len(self.temp_list)==0):
            print('no temperature measurements available ')
        else:
            for i in (self.temp_list):
                print(i,end=" ")

    def addTemp(self,*arguments):
        self.temp_list.extend(arguments)

    def getTemp(self,index):
        if index < len(self.temp_list):
            return self.temp_list[index].temperature

    def getAverage(self):
        return (sum(x.temperature for x in self.temp_list)) / len(self.temp_list)

    def getMaxTemp(self):
        reshima=self.temp_list
        max=self.getTemp(0)
        for i in range(len(self.temp_list)):
            if self.getTemp(i)>max:
                max=self.getTemp(i)
                flag=self.temp_list[i]
        return flag

    def compareLocation(self, temp):
        if self.getAverage() >= temp.getAverage():
            return self
        return temp


#tests
def main():
    d1=Date(1,2,2020)
    d2=Date()
    print(d1,'-',d2)
    t1=Temperature(-12,1,2,2020)
    t2=Temperature(0)
    t3=Temperature(32,20,8,2020)
    print(t1,t2,t3)
    print(t1.compareTemp(t3))

    loc1=Location('London')
    loc1.printLocation()
    loc1.addTemp(Temperature(9), Temperature(7, 1, 12, 2020), Temperature(23, 21, 8, 2020), Temperature(16, 4, 5, 2020))
    loc1.printLocation()
    print()
    print(loc1.getAverage())
    loc1.getAverage()
    print(loc1.getMaxTemp())
    loc2 = Location('Berlin')
    loc2.addTemp(Temperature(6), Temperature(28, 12, 8, 2020), Temperature(3, 1, 12, 2020),Temperature(-3, 2, 1, 2020))
    loc2.printLocation()
    print()
    print(loc2.getAverage())
    print(loc2.compareLocation(loc1).printLocation())

#main()

#part 3

#ex5

#from work 3 ex 5
#ex6 working
def make_sequence(seq=None):
    """create a object and save the data"""
    try:
        if seq is None :
            raise TypeError("no sequence argument")
        elif not (isinstance(seq,tuple) or isinstance(seq,list)):
            raise TypeError("no sequence argument")

    except TypeError as make_seq:
        print("%s:"%type(make_seq), make_seq)
    else:
        seq=tuple(seq)

    def filter(func1=None):
        """filter the sequence according func1, return a tuple"""
        temp_seq=[]
        try:
            if func1==None:
                raise TypeError("No filter function")
        except TypeError as fltr:
            print("%s:"%type(fltr), fltr)
        else:
            for i in range(len(seq)):
                if func1(seq[i]):
                    temp_seq.append(seq[i])
            return tuple(temp_seq)
        finally:
            return seq

    def filter_iterator(func2=None):
        """filter the sequence according func 2 a return a circle sequence, posible change index location by next or reverese"""
        try:
            if func2==None:
                raise TypeError(" No filter function")
        except TypeError as fltr_iter:
            print("%s :"%type(fltr_iter),fltr_iter)
        else:
            tempiteartor = filter(func2)
            index = 0
            flag =False
            degel = False
            def next():
                try:
                    nonlocal index
                    nonlocal flag
                    if func2(tempiteartor[index])and flag==False:
                        print(tempiteartor[index])
                    else:
                        raise IndexError ("%s index out of range"% type(tempiteartor))
                except IndexError as nx:
                    print(nx)
                finally:
                    index = (index + 1) % len(tempiteartor)
                    if index==0:
                        flag=True

            def reverse():
                try:
                    nonlocal index
                    nonlocal degel
                    if func2(tempiteartor[index]) and degel==False:
                        print(tempiteartor[index])
                    else:
                        raise IndexError("%s index error"%type(tempiteartor))
                except IndexError as rv:
                    print(rv)
                finally:
                    index = ((index - 1) % len(tempiteartor))
                    if index==0:
                        degel=True

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

s11=make_sequence((1,2,3,4,5))
print(s11['filter'](lambda x:x%2==0))
s1=make_sequence()
s1=make_sequence('200')
s1=make_sequence((1,2,3,4,5))
print(s1['filter']())
p1=s1['filter_iterator']()
p1=s1['filter_iterator'](lambda x:x<4)
for i in range(6):
    p1['next']()
p1=s1['filter_iterator'](lambda x:x>1)
p1['next']()
p1['next']()
p1['next']()
p1['next']()
print("finshi ")
for j in range(6):
    p1['reverse']()