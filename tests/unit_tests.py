from src.main import is_word_anagram, is_word_valid, find_possible_anagrams, generate_random_word


def test_generate_random_word():
    assert isinstance(generate_random_word(), str)


def test_find_possible_anagrams():

    assert find_possible_anagrams("start") == 35


def test_check_words_are_anagrams():
    assert is_word_anagram("art", "start") is True
    assert is_word_anagram("asd", "test") is False


def test_is_word_valid():
    assert is_word_valid("test") is True
    assert is_word_valid("adasd") is False

