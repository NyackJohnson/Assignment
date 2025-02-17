def slice(S, start=0, end=None):
    if end is None:
        end = len(S)
    return S[start:end]
    
def contains(string, substring):
    index = string.find(substring)
    return index if index != 1 else None

def replace(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring, 1)

def trim(string):
    return string.strip()


def replace_all(s, old, new):
    return s.replace(old, new)