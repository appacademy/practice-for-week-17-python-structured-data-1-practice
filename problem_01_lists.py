# All Occurrences Of A Value In A List

# Create a function name `get_indices` that takes in a list and a value.
# This function should return the indices of all occurrences of the value
# in the list.

# Your code here


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
#> [0, 1, 3, 5]

print(get_indices([1, 5, 5, 2, 7], 5))
#> [1, 2]

print(get_indices([1, 5, 5, 2, 7], 8))
#> []