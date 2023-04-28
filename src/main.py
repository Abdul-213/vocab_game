import random
from collections import Counter
from nltk.corpus import words
from PyMultiDictionary import MultiDictionary


def find_possible_anagrams(main_word: str) -> int:
    words_list = words.words()

    score = 0

    for word in words_list:

        if not is_word_anagram(word, main_word):
            continue

        score += 1

    return score


def is_word_valid(word: str) -> bool:
    dictionary = MultiDictionary()
    if not dictionary.meaning('en', word)[0]:
        return False

    return True


def is_word_anagram(word: str, main_word: str) -> bool:
    word_letter_count = Counter(word)
    main_word_count = Counter(main_word)

    if len(word_letter_count - main_word_count) != 0:
        return False

    return True


def generate_random_word():
    words_list = words.words()
    word = random.choice(words_list)
    while find_possible_anagrams(word) < 10:
        word = random.choice(words_list)

    return word


def game_loop():
    main_word = generate_random_word()
    possible_anagrams_num = find_possible_anagrams(main_word)
    user_words = []
    score = 0

    while True:

        user_input = input(f"Your word is: {main_word}. {possible_anagrams_num} possible anagrams:")

        if user_input == "n":
            break

        if not isinstance(user_input, str):
            print("Incorrect input.")
            continue

        if not is_word_valid(user_input):
            print("Word not valid, please try again.")

        user_words.append(user_input)

    for word in user_words:
        if is_word_anagram(word, main_word):
            score += 1

    print(f"Your score is: {score}")