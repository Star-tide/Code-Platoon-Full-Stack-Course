def sum(*argv):
    for arg in argv:
        print(arg)

def show_me_some_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('%s == %s' % (key, value))

    print(kwargs)

sum(1,2,3,4,5)
show_me_some_kwargs(first="one", second="two", third="three")