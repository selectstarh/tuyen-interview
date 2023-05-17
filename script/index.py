import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helper.normalize_text import normalize_text
from helper.read_file import read_file
from helper.write_file import write_file

def build_indexing(lines):
    line_number = 0
    result = {}

    for line in lines:
        line_number += 1
        words = line.strip().split(' ')
        for word in words:
            normalize_words = normalize_text(word.strip())
            for normalize_word in normalize_words:
                isPresent = normalize_word in result

                if isPresent == True:
                    result[normalize_word]["count"] = result[normalize_word]["count"] + 1
                    result[normalize_word]["lines"].append(line_number)
                else:
                    result[normalize_word] = {}
                    result[normalize_word]["count"] = 1
                    result[normalize_word]["lines"] = [line_number]

    print(result)

    return result

def main():
    file_name_to_read = sys.argv[1]
    file_name_to_write = file_name_to_read.split('.')[0] + '.json'
    text = read_file(file_name_to_read)
    indexes = build_indexing(text.split('\n'))
    write_file(file_name_to_write, indexes)

if __name__ == "__main__":
    main()


