# / means that the parameter/s before gotta be positional
# * means that the parameter after gotta be relational, like number=1 or **{'number': 1}
# this is when we pass it to the function
def combined_example(pos_only, /, standard, *, kwd_only):
    return (pos_only, standard, kwd_only)


# wher we pass parameters as relationals, we gotta pass the key defined in the function
print(combined_example(1, standard=1, kwd_only='fran'))


def write_multiple_items(file, /, separator, *args):
    return separator.join(args)


# using * before a variable means that the variable will unpacked, like '...' on javascript or php languages
# so, if we see it on a function, it means the arguments we pass to it will be packed

write_var = write_multiple_items('cola.js', '.', '12312', '12312', '1231')

# double ** means that the arguments will be packed into a dictionary, i think,
# it actually means that, but we it means we gotta pass key/value pairs to the function
# son parametros relacionales (español)


def say_names(**names):
    return names


names = {
    'name1': 'emiliano',
    'name2': 'francisco',
    'name3': 'miguel'
}

names2 = {**names}
print(['names2', names2])
print(say_names(**names))

# the line on top equal to this
print(say_names(name='1'))

# so we see that the last parameter in the function has *args so the lasts parameter we pass to it will be packed
print(write_var)


# this function prooves if ther is some key that be identical to name
# if there is an attribute name or key on dictionary

def foo(name, /, **kwds):
    example = {'name': name, 'kwds': kwds}
    print([example['name'], example['kwds']])
    return 'name' in example


print(foo(1, **{'name': 2, 'a': 1}))


def tri_recursion(k):
    if (k > 0):
        # print(k + tri_recursion(k - 1))
        print({'value': k})
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        print(k)
        result = 0


print("\n\nRecursion Example Results")
tri_recursion(6)
