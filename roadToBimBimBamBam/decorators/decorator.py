import functools


def uppercase_decorator(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        make_split = func.split()
        return make_split

    return wrapper


@split_string  # 2
@uppercase_decorator  # 1
def say_hi():
    return 'hello there'


print(say_hi.__name__)


def decorator_with_arguments(function):
    def wrapper_with_argument(one, second):
        print(f'{one} {second}')
        function(one, second)

    return wrapper_with_argument


@decorator_with_arguments
def upper(a, b):
    print(a.upper(), b.upper())


def decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)

    return a_wrapper_accepting_arbitrary_arguments


@decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print('No argument there')


@decorator_passing_arbitrary_arguments
def function_with_argument(a, b, c):
    print(a, b, c)


function_with_no_argument()

function_with_argument(1, 2, 4)
