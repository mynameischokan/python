'''
*************************************************
**** Unpacking a Sequence into Separate variables
*************************************************
'''


#########
# Problem
#########
# You have an N-element tuple or sequence that you would like to unpack
# into a collection of N variables.


#########
# Solution
#########
# Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.    # noqa
# The only requirement is that the number of variables and structure match the sequence.    # noqa

# For example:
# >>> p = (4, 5)
# >>> x, y = p

# TODO
# Unpack the following data:
# >>> data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

# Unpacking actually works with any object that happens to be iterable, not just tuples or lists.   # noqa
# TODO
# Unpack the str 'Hello'

# When unpacking, you may sometimes want to discard certain values.
# Python has no special syntax for this, but you can often just pick a throwaway variable name for it.  # noqa
# TODO
# Unpack the data given above by ingnoring first and last items
