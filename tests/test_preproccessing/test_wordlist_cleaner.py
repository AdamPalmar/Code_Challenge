from preproccessing import wordlist_cleaner as wlc


# py.test --cov=test_wordlist_cleaner.py --cov=preproccessing
# --cov-report=term --pep8 --flakes --mccabe


def test_remove_words_with_invalid_char():
    list_of_words = ["olleh", "woldr", "he",
                     "hello_not_valid", "abc", " ", "'", "", "\n"]
    anagram_sentence = "hello world"
    list_of_words_clean = ["olleh", "woldr", "he"]

    result = wlc.remove_words_with_invalid_char(list_of_words,
                                                anagram_sentence)

    assert list_of_words_clean == result


def test_dict_of_char_in_anagram_sentence():
    anagram_sentence = "hello test world"

    expected_dict = {"h": 1,
                     "e": 2,
                     "l": 3,
                     "o": 2,
                     "t": 2,
                     "s": 1,
                     "w": 1,
                     "r": 1,
                     "d": 1}

    result_dict = wlc.dict_of_char_in_anagram_sentence(anagram_sentence)

    assert expected_dict == result_dict


def test_value_to_increment_to_in_dict():
    test_dict = {"a": 1,
                 "b": 2}
    a = 'a'
    b = 'b'
    c = 'c'

    a_result = wlc.value_to_increment_to_in_dict(test_dict, a)
    b_result = wlc.value_to_increment_to_in_dict(test_dict, b)
    c_result = wlc.value_to_increment_to_in_dict(test_dict, c)

    assert a_result == 2
    assert b_result == 3
    assert c_result == 1


def test_remove_words_with_too_many_of_one_char():
    list_of_words = ["hello", "test", "world",
                     "olleh", "tset", "wo", "d",
                     " ", "hellllo", "tesst",
                     "wworld"]

    list_of_words_clean = ["hello", "test", "world",
                           "olleh", "tset", "wo", "d"]

    anagram_sentence = "hello test world"

    result = wlc.remove_words_with_too_many_of_one_char(list_of_words,
                                                        anagram_sentence)

    assert result == list_of_words_clean
