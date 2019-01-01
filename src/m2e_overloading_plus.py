"""
This module demonstrates OVERLOADING the  +  symbol:
  -- With numbers as operands, it means addition (as in arithmetic)
  -- With sequences as operands, it means concatenation, that is,
        forming a new sequence that stitches together its operands.

This module also demonstrates the   STR   function.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, and their colleagues.
"""
# -----------------------------------------------------------------------------
#  Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
#           Before you leave this example,
#   *** MAKE SURE YOU UNDERSTAND:                         ***
#   ***   -- What it means to use   +   for CONCATENATION ***
#   ***   -- What the   str   function does.              ***
# -----------------------------------------------------------------------------


def main():

    """ Demonstrates OVERLOADING the  +  symbol. """
    # -------------------------------------------------------------------------
    # First example below:  computes 5 + 33 (addition, as in arithmetic)
    # Second example below: stitches together the two lists.
    # Third example below:  stitches together the three tuples.
    # Fourth example below: stitches together the four strings.
    # Fifth example: contrasts concatenation with addition.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Addition, then various forms of concatenation:')
    print('-----------------------------------------------------------')

    print(5 + 33)
    print([4, 3] + [1, 7, 2, 4])
    print((4, 1, 7) + (444,) + (3, 3))
    print('hello' + 'Dave' + '55' + '83')
    print(5 + 33, '5' + '33')

    # -------------------------------------------------------------------------
    # The  str  function and the concatenation form of the  +  operator
    # are handy for making strings from sub-strings.  For example:
    # -------------------------------------------------------------------------
    x = 51
    y = 3
    z = 40

    print()
    print('-----------------------------------------------------------')
    print('With and (using string concatenation) without spaces:')
    print('-----------------------------------------------------------')

    # -------------------------------------------------------------------------
    # Printing multiple items puts spaces between the items.
    # That is usually what you want.
    # -------------------------------------------------------------------------
    print(x, y, z)

    # -------------------------------------------------------------------------
    # But if you don't want spaces
    # (or want to otherwise format the string result):
    # -------------------------------------------------------------------------

x = []
for k in range(5):
     x = x + [(2 * k)]
print(x)