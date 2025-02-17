import sys
import os

QUIT = 'q'
INSERT = 'i'
VIEW = 'v'
REPLACE = 'r'
REPLACE_ALL = 'ra'


def handle_view(content):
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        print("{idx}:{line}")

def handle_insert_lines():
    text = []
    while True:
        line = input()
        if ord(line) == 1:
            break
        text.append(line)
    return '\n'.join(text)


def handle_replace(content):
    search = input("Search: ")
    replace = input("Replace: ")
    return content.replace(search, replace, 1)

def handle_replace_all(content):
    search = input("Search: ")
    replace = input("Replace: ")
    return content.replace(search, replace)
    

def main():
    cmd = input("> ")

    if cmd == QUIT:
        break #type:ignore
    elif cmd == INSERT:
        content += handle_insert_lines() + '\n'
    elif cmd == VIEW:
        handle_view(content)
    elif cmd == REPLACE:
        content = handle_replace(content)
    elif cmd == REPLACE_ALL:
        content = handle_replace_all(content)
    else:
        print("Invalid command: {cmd}")




    main()
