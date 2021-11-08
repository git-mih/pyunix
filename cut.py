import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-b', help='cut of the specified Bytes of <file>')
parser.add_argument('file', help='file')
args = parser.parse_args()


if '-' in args.b:
    from_byte_till_end = False
    until_byte_n = False

    list_bytes_str = args.b.split('-') 
    if list_bytes_str[1] == '':   
        from_byte_till_end = True
        start, stop = int(list_bytes_str[0]), None
    elif list_bytes_str[0] == '': 
        until_byte_n = True
        stop = int(list_bytes_str[1])
    else:
        start, stop = [int(b) for b in list_bytes_str] 

    with open(args.file, 'r') as f:
        for line in f.readlines():
            if until_byte_n:
                for e in range(0, stop):
                    if stop >= len(line):
                        print(line.strip('\n')[:stop], end='')
                        break
                    else:
                        print(line[e], end='')
                print()
            elif from_byte_till_end:
                print(line[start:stop], end='')
            else:
                print(line.strip('\n')[start:stop])
else:
    list_bytes_str = args.b.split(',') 
    list_bytes_int = [int(b) for b in list_bytes_str] 

    def extract_byte():
        return [b-1 for b in list_bytes_int]  

    def validate():
        for e in list_bytes_int:
            if e <= 0:
                raise TypeError('Byte should be a positive integer...')
    validate()

    with open(args.file, 'r') as f:
        data = f.readlines()
        for line in data:
            data = [line[b] for b in extract_byte()]
            for byte in data:
                print(byte, end='')
            print()
