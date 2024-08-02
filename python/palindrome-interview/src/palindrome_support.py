import re
from functools import singledispatch
from collections import Counter
from typing import Optional


_INVALID_CHARACTERS_PATTERN = re.compile(r"[^a-zA-Z]")


@singledispatch
def is_not_palindrome_candidate(data) -> bool:
    return True


@is_not_palindrome_candidate.register
def _(data: str) -> bool:

    if data == None or len(data) == 0:
        return True
    return bool(_INVALID_CHARACTERS_PATTERN.search(data))


@is_not_palindrome_candidate.register
def _(frequency_of_character_map: dict) -> bool:

    unpaired_count = sum(
        1
        for frequency_of_character in frequency_of_character_map.values()
        if frequency_of_character % 2 == 1
    )
    return unpaired_count > 1


def to_character_frequency_map(data: str) -> dict:
    return dict(Counter(data))


def character_frequency_map_to_palindrome(character_frequency_map: dict) -> str:

    palindrome_length = Counter(character_frequency_map).total()

    palindrome = ["" for _ in range(palindrome_length)]

    position = 0

    for character, frequency in character_frequency_map.items():
        if frequency % 2 == 1:
            palindrome[palindrome_length // 2] = character
            frequency -= 1

        while frequency > 0:
            palindrome[position] = character
            palindrome[-(position + 1)] = character
            position += 1
            frequency -= 2

    return "".join(palindrome)


def make_palindrome_from(data: str) -> Optional[str]:

    if is_not_palindrome_candidate(data):
        return None

    character_frequency_map = to_character_frequency_map(data)

    if is_not_palindrome_candidate(character_frequency_map):
        return None

    return character_frequency_map_to_palindrome(character_frequency_map)
