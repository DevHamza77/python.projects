import sys

if len(sys.argv) < 2:
   sys.exit("too few arguments")
elif len(sys.argv) > 2:
   sys.exit("too many arguments")

print("Hello, " + sys.argv[1])
   
# 'sys' library has been imported 
# condition is given that 
# if the value is more than two values, say too few arguments and exit the system
# if it is more than 2 values, say too many argumebts and exit the system
# this indicates that the value of sys.argv will only be printed if its equal to 2