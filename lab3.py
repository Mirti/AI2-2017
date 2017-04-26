def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))

def print_two_test():
   # print_two() invalid
    print_two(4, 1)
   # print_two(41) invalid
   # print_two(a=4, 1) error
   # print_two(4, a=1) invalid
   # print_two(4, 1, 1) invalid
   # print_two(b=4, 1) error
    print_two(a=4, b=1)
    print_two(b=1, a=4)
   # print_two(1, a=1) error
   # print_two(4, 1, b=1) error

def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

def print_keyword_args():
    keyword_args(5)
    keyword_args(a=5)
    keyword_args(5, 8)
    keyword_args(5, 2, c=4)
    keyword_args(5, 0, 1)
    keyword_args(5, 2, d=8, c=4)
   # keyword_args(5, 2, 0, 1, "")  invalid
   # keyword_args(c=7,1) no compile
    keyword_args(c=7, a=1)
    keyword_args(5, 2, [], 5)
   # keyword_args(1, 7, e=6) invalid
    keyword_args(1, c=7)
   # keyword_args(5, 2, b=4) invalid

def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

def print_variadic():
    variadic(2, 3, 5, 7)
    variadic(1, 1, n=1)
   # variadic(n=1,2, 3) no compile
    variadic()
    variadic(cs="Computer Science", pd="Product Design")
  #  variadic(cs="Computer Science", cs="CompSci", cs="CS") no compile
    variadic(5, 8, k=1, swap=2)
    variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
    variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
    variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
    variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)
    
def print_all_together():
  #  all_together(2)  invalid
    all_together(2, 5, 7, 8, indent=False)
    all_together(2, 5, 7, 6, indent=None)
  #  all_together() 
  #  all_together(indent=True, 3, 4, 5) no compile
  #  all_together(**{'indent': False}, scope='maximum') invalid
    all_together(dict(x=0, y=1), *range(10))
   # all_together(**dict(x=0, y=1), *range(10)) invalid
   # all_together(*range(10), **dict(x=0, y=1)) invalid
    all_together([1, 2], {3:4})
   # all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'}) invalid
    all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
    all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})


def speak_excitedly(text, wykrzykniki=1, emocje=False):
    text += '!' * wykrzykniki
    if not emocje:
        return text
    return text.upper()

def average(*numer):
    if not numer: return None
    return sum(numer) / len(numer)

def make_table(key_justify='left', value_justify='right', **kwargs):
    # Map from human-readable justifications to .format alignment specifiers
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        print("Error! Invalid justification specifier.")
        return None

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(map(len, kwargs.keys()))
    max_value_length = max(map(len, kwargs.values()))

    total_length = 2 + max_key_length + 3 + max_value_length + 2
    print('=' * total_length)
    for key, value in kwargs.items():
        print('| {:{key_align}{key_pad}} | {:{value_align}{value_pad}} |'.format(key, value,
            key_align=key_alignment_specifier, key_pad=max_key_length,
            value_align=value_alignment_specifier, value_pad=max_value_length
        ))
    print('=' * total_length)

def test_make_table():
    make_table(
        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink"
    )

    make_table(
        key_justify="right",
        value_justify="center",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
    )

