import argparse
import sys
import os

parser = argparse.ArgumentParser(description="cat.py - Concatenate FILE(s) to stdout.")
parser.add_argument('inputs', nargs='*', type=argparse.FileType('r', encoding='utf-8'), help='will concatente together each input. can be used without any input, in this case, it will prompt the user to provide values to be displayed/redirected to a file.')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if args.inputs:
    os.system('cls')
    for file in args.inputs:
        print(file.read(), end='\n\n') 
        file.close()
else:
    msg = sys.stdin.readlines()
    for line in msg:
        print(line, end='')

print()
