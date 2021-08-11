
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner

div=smart_div(div)

div(2,4)

"""decorators--
they are used modify function of class without access outside of the class 
here if you wnat to add a condition when a<b then swap then you write it in the class 
directly but what if i say you arent allow to do so  how can you made change to class
without enter in it 
by using the decorators """