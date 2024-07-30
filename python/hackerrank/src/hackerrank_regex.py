"""
See also
- https://developers.google.com/edu/python/regular-expressions
- https://docs.python.org/3/library/re.html
"""

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

def replace_and_or(data) -> str:

    and_regex = r'(?<= )(&)\1(?= )'
    or_regex = r'(?<= )(\|)\1(?= )'

    data = re.sub(and_regex, 'and', data)
    data = re.sub(or_regex, 'or', data)

    return data

code =  '''
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
replace_and_or
'''

lines = code.splitlines()

for line in lines:
    updated_line = replace_and_or(line)
    print(updated_line)


# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true

def is_valid_roman_number(data) -> bool:
    
        regex = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    
        m=re.match(regex, data)
    
        return m is not None

print(is_valid_roman_number('CDXXI'))


# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

def is_valid_phone_number(data) -> bool:
    regex = r'^[789][0-9]{9}$'
    if re.match(regex, data):
        return True
    return False

for s in ['9587456281', '1252478965', '1234567890', '9876543210']:
    if is_valid_phone_number(s):
        print('YES')
    else:
        print('NO')

# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

def is_valid_credit_card_number(data) -> bool:

    valid_regex = r'^(?=[456])([0-9]{4}-?){3}[0-9]{4}$'
    repeated_regex = r'([0-9])\1{3,}'

    if not re.match(valid_regex, data):
        return False
    
    data = data.replace('-', '')

    if re.search(repeated_regex, data):
        return False
    
    return True

for card in [
    '4123456789123456', 
    '5123-4567-8912-3456', 
    '61234-567-8912-3456', 
    '4123356789123456', 
    '5133-3367-8912-3456', 
    '5123 - 3567 - 8912 - 3456',
    '3695-7963-  5827-75',
    '4143-4672-8798-2968-2968',
    '6865---------------3965---------------1564-------------2918',
    '6865396515642918']:
    if is_valid_credit_card_number(card):
        print('YES')
    else:
        print('NO')

# https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true

def is_valid_postal_code(data) -> bool:

    regex_integer_in_range = r"^(?=[1-9])[0-9]{6}$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

    integer_in_range = bool(re.match(regex_integer_in_range, '123456'))
    alternating_repetitive_digit_pair_count = re.findall(regex_alternating_repetitive_digit_pair, '110100')
    alternating_repetitive_digit_pair_count = re.findall(regex_alternating_repetitive_digit_pair, '110000')

    return ( integer_in_range and len(alternating_repetitive_digit_pair_count) < 2 )

is_valid_postal_code('110000')