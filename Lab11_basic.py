#HW4 ex3 account!!!!!!!!!!

### Our custom OOP
def make_class(attrs,name, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    #print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value

        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    #------------ i added!!!!!!!!!!!!!!!!!!
    cls['set']('name',name)
    cls['set']('class',cls)

    return cls

# i write!!!!!!!!!!!
def make_account_class():

    def __init__(self,ribit=0.05):
        self.interest=ribit
    return make_class(locals(), 'Account', {'interest' : 0.05})
#return make_class(locals(),'Point')#Ex2------ ,'Point'

# def make_save_account_class():
#     def init(self, owner):
#         self['set']('owner', owner)
#         self['set']('balance', 0)
#     return make_class(locals(),'SaveAccount',{'__init__': init, 'interest': 0.03}, Account)


def driver():
    print(Account['get']('name'))
    # print(SaveAccount['get']('name'))


Account = make_account_class()
# SaveAccount = make_save_account_class()
driver()


