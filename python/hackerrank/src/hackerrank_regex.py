import re

# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

def find_first_repeating_character(data):

    m=re.search(r"([A-Za-z0-9])\1", data )

    print(m.group(1))

find_first_repeating_character('__commit__')


# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

def find_vowel_sequences(data):

    m=re.findall(r"(?<=[^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])", data)

    if not m:
        print(-1)
        return

    for i in m:
        print(i)

find_vowel_sequences("rabcdeefgyYhFjkIoomnpOeorteeeeet")


# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

def verify_floating_point_number(data) -> bool:

    regex = r'^[+-]?[0-9]*\.[0-9]+$'

    m=re.match(regex, data)

    if not m:
        return False
    
    try:
        float_number = float(m.group(0))
        return True
    except (ValueError, TypeError):
        return False

for s in ['1.414', '+.5486468', '0.5.0', '1+1.0', '0']:
    print(verify_floating_point_number(s))


# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

def find_start_and_end_indices(s, k):

    if not s or len(s) == 0 or not k or len(k) == 0:
        print((-1, -1))
        return

    if len(k) >= len(s):
        print((-1, -1))
        return

    regex = r'(?=('+re.escape(k)+'))'

    m_iter=re.finditer(regex, s)

    found = False
    for m in m_iter:
        found = True
        print((m.start(), m.start() + len(k) - 1))
    
    if not found:
        print((-1, -1))

    return

find_start_and_end_indices('jjhv', 'z')

# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true