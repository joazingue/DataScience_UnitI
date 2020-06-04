def dude_decorator(func):
    def inner_func():
        func()
        print('Dude!')
    return inner_func()

@dude_decorator
def howyadoin():
    print('How are you?')