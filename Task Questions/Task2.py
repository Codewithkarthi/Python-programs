#method(1)
#combinations of the letters "a," "b," and "c" without repetition.
#you can use the combinations function from the itertools module.


from itertools import combinations

letters = ['a', 'b', 'c']

combinations_list = []
for r in range(1, len(letters) + 1):
    combinations_list.extend(combinations(letters, r))

combinations_result = [''.join(combination) for combination in combinations_list]

print(combinations_result)

#method(2)
#simple method of combinating letters in python.

from itertools import permutations

letters = ['a', 'b', 'c']

combinations = [''.join(p) for p in permutations(letters)]

print(combinations)
