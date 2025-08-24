#!/usr/bin/python
import sys
import argparse
import fileinput
import os

def count(inputStream):
    """
    Return statistics of the stream as a dict.
    """
    data = inputStream.read()

    return {
        "lines": data.count("\n"),
        "words": len(data.split()),
        "chars": len(data),
        "bytes": len(data.encode("utf-8")),
    }
  
    return line_count, word_count, char_count, byte_count

def get_result(stats: dict, args, file_name: str | None = None):
    """
    Pick values from stats based on flags.
    """
    if args.bytes:
        result = [stats["bytes"]]
    elif args.lines:
        result = [stats["lines"]]
    elif args.words:
        result = [stats["words"]]
    elif args.chars:
        result = [stats["chars"]]
    else:
        result = [stats["lines"], stats["words"], stats["bytes"]]

    if file_name:
        result.append(file_name)

    return result


def process_files(files, args):
    """
    Process multiple files and return list of results.
    """
    return [get_result(count(f), args, f.name) for f in files]


def process_input(input_stream, args):
    """
    Process standard input and return result.
    """
    return get_result(count(input_stream), args)

def main(args):
    """
    Main driver function. Processes input based on whether stdin or files are used.
    """
    output = None

    # Determine the source type
    if args.file != sys.stdin:
        output = process_files(args.file, args)
    else:
        output = process_input(sys.stdin, args)

    return output

def display_output(output: str | list):
    """ 
    Displays output by formatting accordingly 
    """

    if isinstance(output, list):
        if(isinstance(output[0], list)):
            for line in output:
                print(" ".join(str(item) for item in line))
        else:
            print(" ".join(str(item) for item in output))
    else:
        print(str(output))


# Driver code
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='replicate the wc tool(linux)')
    parser.add_argument('-c', '--bytes',help = 'option to count number of bytes in file', action='store_true')
    parser.add_argument('-l', '--lines',help = 'option to count number of lines in file', action='store_true')
    parser.add_argument('-w', '--words',help = 'option to count number of words in file', action='store_true')
    parser.add_argument('-m', '--chars',help = 'option to count number of characters in file', action='store_true')
    # expects optional input-files if provided, else standard input
    parser.add_argument('file', nargs='*', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
    args = parser.parse_args()


    output = main(args)
    display_output(output)
    sys.exit(0)
