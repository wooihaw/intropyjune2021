# Make a function animal that, given a string, returns 'antelope'
# if the string starts with an a.  Otherwise, return 'zebra'.
#
# >>>> animal("arg")
# antelope
# >>>> animal("python")
# zebra

def animal(string):
# Add code here that returns the answer
    if string[0] == 'a':
        ans = 'antelope'
    else:
        ans = 'zebra'
    return ans
  
# Add print statements here to test what your code does:
print(animal("arg"))
print(animal("python"))