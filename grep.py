import glob
import argparse
import re
import os

parser =  argparse.ArgumentParser()
parser.add_argument('-i', action='store_true') 
parser.add_argument('-n', action='store_true') 
parser.add_argument('-w', action='store_true') 

parser.add_argument('match_str')
parser.add_argument('path')
args = parser.parse_args()


paths = glob.glob(args.path, recursive=True) 

for path in paths:
    if os.path.isfile(path):
        with open(path, 'r') as f:
            text = f.readlines()
            pattern = args.match_str 
            line_number = 0

            if args.i:
                for line in text:
                    line_number += 1 
                    matches = re.finditer(pattern, line, re.I) 
                    if matches:
                        if args.w:  
                            for m in matches:
                                if args.n:
                                    print(f'{path}: {line_number}: {m[0]}')
                                else:
                                    print(f'{path}: {m[0]}')
                        else: 
                            for _ in matches:
                                if args.n:
                                    print(f'{path}: {line_number}: {line}', end='')
                                else:
                                    print(f'{path}: {line}', end='')
            else:
                for line in text:
                    matches = re.finditer(pattern, line)
                    if matches:
                        if args.w:
                            for m in matches:
                                if args.n:
                                    print(f'{path}: {line_number}:{m[0]}')
                                else:
                                    print(f'{path}: {m[0]}')
                        else: 
                            for _ in matches:
                                if args.n:
                                    print(f'{path}: {line_number}:{line}', end='')
                                else:
                                    print(f'{path}: {line}', end='')
    

