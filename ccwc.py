#!/usr/bin/python
import sys
import argparse
import fileinput
import os
# import locale
# locale.setlocale(locale.LC_ALL, '')
# print(f"Locale setting = ${locale.getlocale}")


def count(file):
    """
    Counts lines, words, and characters in a given file-like object.
    """
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0

    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)
    file.seek(0)
    file_content = file.read()
    byte_count = len(file_content.encode('utf-8'))

    return line_count, word_count, char_count, byte_count

def process_file(file, args):
    """
    Process a single file and return count result based on args.
    """
    line_count, word_count, char_count, byte_count = count(file)

    if args.bytes:
        return [byte_count, file.name]
    elif args.lines:
        return [line_count, file.name]
    elif args.words:
        return [word_count, file.name]
    elif args.chars:
        return [char_count, file.name]
    else:
        return [line_count, word_count, byte_count, file.name]

def process_files(files, args):
    """
    Process multiple files and return list of results.
    """
    results = []

    for f in files:
        result = process_file(f, args)
        results.append(result)

    return results

def main(args):
    """
    Main driver function. Processes input based on whether stdin or files are used.
    """
    output = None

    # Determine the source type
    if args.file != sys.stdin:
        output = process_files(args.file, args)
    else:
        # Placeholder for stdin handling
        pass

    return output

def display_output(output: str | list):
    """ 
    Displays output by formatting accordingly 
    """

    if isinstance(output, list):
        for line in output:
            if isinstance(line, list):
                print(" ".join(str(item) for item in line))
            else:
                print(str(line))
    else:
        print(str(output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='replicate the wc tool(linux)')
    parser.add_argument('-c', '--bytes',help = 'option to count number of bytes in file', action='store_true')
    parser.add_argument('-l', '--lines',help = 'option to count number of lines in file', action='store_true')
    parser.add_argument('-w', '--words',help = 'option to count number of words in file', action='store_true')
    parser.add_argument('-m', '--chars',help = 'option to count number of characters in file', action='store_true')
    # expects optional input-files if provided, else standard input
    parser.add_argument('file', nargs='*', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()


    output = main(args)
    display_output(output)
    sys.exit(0)
