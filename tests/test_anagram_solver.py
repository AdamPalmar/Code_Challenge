import pytest
from md5_hashing import md5_hasher
from fileIO import file_reader

def test_is_sentence_an_anagram_with_hashing_md5():
    sentence = "poultry outwits ants"
    hashed_sentence = md5_hasher.md5_hash_sentence(sentence)
    print(hashed_sentence)
    assert hashed_sentence == '4624d200580677270a54ccff86b9610e'

def test_hash_every_sentence_in_file_with_md5():
    list_of_sentences = file_reader.read_file_into_list("../wordlist")
    for sentence in list_of_sentences:
        hashed_sentence = md5_hasher.md5_hash_sentence(sentence)
        if hashed_sentence == "4624d200580677270a54ccff86b9610e":
            print(sentence)


