import hashlib


def md5_hash_sentence(sentence):
    return hashlib.md5(sentence.encode('utf-8')).hexdigest()


