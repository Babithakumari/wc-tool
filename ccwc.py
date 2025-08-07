#!/usr/bin/python
import sys
import argparse

# import locale
# locale.setlocale(locale.LC_ALL, '')
# print(f"Locale setting = ${locale.getlocale}")


def count_bytes(filePath: str) -> int:
    """Reads the file and outputs number of bytes"""
    try:
        with open(filePath, 'rb') as f:
            read_data = f.read()
        return len(read_data)
    except Exception as e:
        raise RuntimeError('Error occured during runtime')

def count_lines(filePath: str) -> int:
    """Reads the file and outputs number of lines in the file"""
    try:
        with open(filePath, 'rb') as f:
            read_data = f.readlines()
        return len(read_data)
    except Exception as e:
        raise RuntimeError('Error occured during runtime')

def count_words(filePath: str) -> int:
    """Reads the file and outputs number of words in the file"""
    try:
        with open(filePath, 'r') as f:
            read_data = f.read()
        return len(read_data.split())
    except Exception as e:
        raise RuntimeError('Error occured during runtime')

def count_chars(filePath: str) -> int:
    """Reads the file and outputs number of characters in the file"""
    try:
        with open(filePath, 'r', encoding="utf-8") as f:
            words = 0
            chars = 0
            lines = 0
            # read_data 
            # for line in f:
            #     print(f"line length = {len(line)}")
            #     chars += len(line)
            #     print(f"char length = {chars}")
                #read_data += len(line)
            read_data = f.read()
        return len(read_data)
        return chars
    except Exception as e:
        raise RuntimeError('Error occured during runtime')


if __name__ == '__main__':
    # expects 1 argument - the name of the file to read from

    parser = argparse.ArgumentParser(description='replicate the wc tool(linux)')
    parser.add_argument('-c', '--bytes',help = 'option to count number of bytes in file', action='store_true')
    parser.add_argument('-l', '--lines',help = 'option to count number of lines in file', action='store_true')
    parser.add_argument('-w', '--words',help = 'option to count number of words in file', action='store_true')
    parser.add_argument('-m', '--chars',help = 'option to count number of characters in file', action='store_true')
    parser.add_argument('file', help = 'path of the file to be read')

    args = parser.parse_args()

    if(args.bytes):
        result = count_bytes(args.file)
    elif(args.lines):
        result = count_lines(args.file)
    elif(args.words):
        result = count_words(args.file)
    elif(args.chars):
        result = count_chars(args.file)
    else:
        result = count_bytes(args.file) 

    print(result)
    sys.exit(0)

