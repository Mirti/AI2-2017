import operator
import functools
import itertools

def test_lambda():
  print((lambda val: val ** 2)(5)) 
  print((lambda x, y: x * y)(3, 8)) 
  print((lambda s: s.strip().lower()[:2])('  PyTHon'))  

def test_map():
    print(list(map(int, ('10110', '0xCAFE', '42'), (2, 16, 10))))
    print(list(map(int, ['12', '-2', '0'])))
    print(list( map(len, ['hello', 'world'])))
    print(list(map(lambda x: x[::-1], ['hello', 'world'])))
    print(list(map(lambda n: (n, n ** 2, n ** 3), range(2, 6))))
    print(list(map(lambda l, r: l * r, range(2, 5), range(3, 9, 2))))

def test_filter():
    print(list((filter(lambda x: int(x) >= 0, ['12', '-2', '0']))))
    print(list( filter(lambda x: x == 'world', ['hello', 'world'])))
    print(list( filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])))
    print(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return functools.reduce(lambda x, y: x * y / gcd(x, y), args)


def test_operator():
    print(operator.add(1,2))
    print(operator.mul(3, 10))
    print(operator.pow(2, 3))
    print(operator.itemgetter(1)([1, 2, 3]))

def fact(n):
    return functools.reduce(operator.mul, range(1,n+1))

def test_ord():
    words = ['pear', 'cabbage', 'apple', 'bananas']
    print(min(words))  
    words.sort(key=lambda s: s[-1])  
    print(words) 
    print(max(words, key=len))
    print(min(words, key=lambda s: s[1::2]))

def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

def test_two_best():
    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))


def float_Control(score):
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"

def replace_Return(*args):
  echo = lambda arg: arg  
  cond_fn = lambda x: (x==1 and print("one")) \
                 or (x==2 and print("two")) \
                 or (print("other"))

def replace_Loop(lst,func):
  map(func,lst)


def iterator_Consumption():
  it = iter(range(100))
  print(67 in it)  # => True
  print(next(it))  # => 68
  (37 in it)  # => Error
  (next(it))  # => StopIteration

def test_itertools():
    for el in itertools.permutations('XKCD', 2):
        print(el, end=', ')

    for el in itertools.cycle('LO'):
        print(el, end='')  # Don't run this one. Why not?

    itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))

def dot_product(u, v):
    assert len(u) == len(v)
    return sum(itertools.starmap(operator.mul, zip(u, v)))

def transpose(m):
    return tuple(zip(*m))

def test_transpose():
    matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12)
    )
    print(transpose(matrix))

def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total


def primes_under(n):
    tests = []
    for i in range(2, n):
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
            yield i

"""
def outer():
    def inner(a):
        return a
    return inner

f = outer()
print(f)  # <function outer.<locals>.inner at 0x1044b61e0>
f(10)  # => 10

f2 = outer()
print(f2)  # <function outer.<locals>.inner at 0x1044b6268> (Different from above!)
f2(11)  # => 11
"""

def make_adder(n):
    def add_n(m):  # Captures the outer variable `n` in a closure
        return m + n
    return add_n

def test_make_adder():
    add1 = make_adder(1)
    print(add1)  # <function make_adder.<locals>.add_n at 0x103edf8c8>
    add1(4)  # => 4
    add1(5)  # => 6
    add2 = make_adder(2)
    print(add2)  # <function make_adder.<locals>.add_n at 0x103ecbf28>
    add2(4)  # => 6
    add2(5)  # => 7
    
    closure = add1.__closure__
    cell0 = closure[0]
    cell0.cell_contents  # => 1 (this is the n = 1 passed into make_adder)

def foo(a, b, c=-1, *d, e=-2, f=-3, **g):
    def wraps():
        print(a, c, e, g)

def test_foo():
    w = foo(1, 2, 3, 4, 5, e=6, f=7, y=2, z=3)
    print(list(map(lambda cell: cell.cell_contents, w.__closure__)))

def outer(l):
    def inner(n):
        return l * n
    return inner

def test_outer():
    l = [1, 2, 3]
    f = outer(l)
    print(f(3))
    l.append(4)
    print(f(3))

def print_args(function):
    def wrapper(*args, **kwargs):
        # (1) You could do something here
	    retval = function(*args, **kwargs)
		# (2) You could also do something here
	    return retval
    return wrapper

@cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

def test_fib():
    fib(10)  # 55 (takes a moment to execute)
    fib(10)  # 55 (returns immediately)
    fib(100) # doesn't take forever
    fib(400) # doesn't raise RuntimeError

@enforce_types
def foo2(a: int, b: str) -> bool:
    if a == -1:
        return 'Gotcha!'
    return b[a] == 'X'

def test_foo2():
    foo(3, 'abcXde')  # => True
    foo(2, 'python')  # => False
    foo(1, 4)  # prints "Invalid argument type for b: expected str, received int
    foo(-1, '')  # prints "Invalid return type: expected bool, received str

@enforce_types(severity=2)
def bar(a: list, b: str) -> int:
    return 0

@enforce_types()  # Note that there are parentheses
def baz(a: bool, b: str) -> str:
    return ''
    

