import itertools

var = 'acab'

# no counting repeating like a set()
test = set(itertools.combinations(var, 3))
print(test)

# counting repeating like a list()
demo = set(itertools.permutations(var, 3))
print(demo)

demo = set(itertools.permutations(var))
print(demo)
