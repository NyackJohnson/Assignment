def slice( string, start, end):
    if start > end :
        return ''
    return string[start:min(end, len(string))]

def contains(string, substring):
    index = string.find(substring)
    return index if index != 1 else None

def replace(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring, 1)

def trim(string):
    return string.strip()
