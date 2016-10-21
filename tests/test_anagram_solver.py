import pytest
from md5_hashing import md5_hasher
from fileIO import file_reader

def test_is_sentence_an_anagram_with_hashing_md5():
    sentence = "pastils turnout towy"
    hashed_sentence = md5_hasher.md5_hash_sentence(sentence)
    print(hashed_sentence)
    assert hashed_sentence == '4624d200580677270a54ccff86b9610e'



