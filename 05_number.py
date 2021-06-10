# Make a function how_many that, given a list of a number
# and a thing name, returns a grmmatically correct sentence
# describing the number of things.
#
# >>>> how_many([5, "python"])
# There are 5 pythons.
# >>>> how_many([1, "king"])
# There is 1 king.

def how_many(the_list):
  # Add code here that returns the answer
  if the_list[0] > 1:
      ans = 'There are ' + str(the_list[0]) + ' ' + the_list[1] +'s.'
  else:
      ans = 'There is ' + str(the_list[0]) + ' ' + the_list[1] +'.'
  return ans
  
# Add print statements here to test what your code does:
print(how_many([5, "python"]))
print(how_many([1, "king"]))
print(how_many([2, "snake"]))