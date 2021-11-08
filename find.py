import argparse
import pathlib
import glob

parser = argparse.ArgumentParser()

parser.add_argument('-print', action='store_true', required=False)
parser.add_argument('-name')
parser.add_argument('-type', choices=['d', 'f'])
parser.add_argument('path')

args = parser.parse_args()


pathlib.Path()
if args.print:
    if args.name:
        path = pathlib.Path(args.path) 
        for p in path.glob(f'**/{args.name}'):
            if args.type == 'd':
                if p.is_dir():
                    print(p)
            elif args.type == 'f':
                if p.is_file():
                    print(p)
            else:
                print(p)
    else:
        path = pathlib.Path(args.path)
        if args.path == '.':
            for p in path.glob('**/*'):
                if args.type == 'd' and p.is_dir():
                    print(p)
                elif args.type =='f' and p.is_file():
                    print(p)
                else:
                    print(p)
        else:
            for i in path.iterdir():
                print(i)
                for p in glob.glob(f'{i}/*'):
                    print(p)
else:
    print('no')











