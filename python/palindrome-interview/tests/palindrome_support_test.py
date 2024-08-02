from palindrome_support import (
    to_character_frequency_map,
    character_frequency_map_to_palindrome,
    is_not_palindrome_candidate,
    make_palindrome_from,
)


def test_is_not_palindrome_candidate_when_data_is_not_supported_type():
    assert is_not_palindrome_candidate(int(1))


def test_is_not_palindrome_candidate_when_data_is_null():
    assert is_not_palindrome_candidate(None) == True


def test_is_not_a_palindrome_candidate_when_data_is_empty():
    assert is_not_palindrome_candidate("") == True


def test_is_not_a_palindrome_candidate_when_data_has_any_invalid_characters():
    assert is_not_palindrome_candidate("abc1def") == True
    assert is_not_palindrome_candidate("_") == True
    assert is_not_palindrome_candidate("ab cd") == True


def test_is_a_palindrome_candidate_when_data_has_only_valid_characters():
    assert is_not_palindrome_candidate("a") == False
    assert is_not_palindrome_candidate("abc") == False


def test_is_not_a_palindrome_candidate_when_more_than_one_character_is_unpaired():
    assert is_not_palindrome_candidate({"a": 2, "b": 1, "c": 3})


def test_is_a_palindrome_candidate_when_at_most_one_character_is_unpaired():
    assert is_not_palindrome_candidate({"a": 2, "b": 2, "c": 3}) == False
    assert is_not_palindrome_candidate({"a": 2, "b": 2}) == False


def test_frequency_of_character_map_1():
    assert to_character_frequency_map("a") == {"a": 1}
    assert to_character_frequency_map("ab") == {"a": 1, "b": 1}
    assert to_character_frequency_map("aab") == {"a": 2, "b": 1}
    assert to_character_frequency_map("aabb") == {"a": 2, "b": 2}
    assert to_character_frequency_map("aabbcc") == {"a": 2, "b": 2, "c": 2}
    assert to_character_frequency_map("abcccbaddddd") == {
        "a": 2,
        "b": 2,
        "c": 3,
        "d": 5,
    }


def test_frequency_of_characters_map_to_palindrome_1():
    assert character_frequency_map_to_palindrome({"a": 2, "b": 2}) == "abba"
    assert (
        character_frequency_map_to_palindrome({"a": 2, "b": 5, "c": 2}) == "abbcbcbba"
    )


def test_make_palindrome_from_1():
    assert make_palindrome_from("abab") == "abba"
    assert make_palindrome_from("a") == "a"
    assert make_palindrome_from("abcdaaabbbcccddde") == "aabbccddeddccbbaa"
    assert make_palindrome_from("") == None
    assert make_palindrome_from(None) == None
    assert make_palindrome_from("abcd") == None
    assert make_palindrome_from("11233") == None
    assert make_palindrome_from("ab.ba") == None
