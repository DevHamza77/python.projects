import argparse

parser = argparse.ArgumentParser( description="meow like a cat" )
parser.add_argument( "number",default =1, type=int, help="Number of meows" )
args= parser.parse_args()

for _ in range(args.number):
    print("Meow")