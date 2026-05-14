import cowsay
import sys 

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])

# Libraries ' cowsay ' and ' sys ' are imported
# condition is given if the length of sys.argv is equal to 2 then would the cow say something