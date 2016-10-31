## Anagram Solver
## The problem
I see the problem as two folded.

- Find words that is an anagram of the sentence
- The specific anagram must hash to a specific hash 

## Anagram definition
https://en.wikipedia.org/wiki/Anagram.
An anagram is made by rearranging the letters of a word or sentence such that a new word or phrase is created.


##Program
The current program can find anagram sentences of combinations of 3 words or less from a word list.

I have focused on optimizing the search for anagram sentences hashes for 1, 2 or 3 words.
Also to make tests that cover the program code.


## Steps in program
###Preprocessing

At first the program does preprocessing on the wordlist removing not viable words.
This is done by removing words with characters that cannot be found in the anagram sentence.

Afterwards the individual characters in the words are mapped to prime numbers.


###Processing

The processing is then distributed to 4 processes.

The processing loop consists of elementwise array multiplication of the combinations of word prime number representation.
Afterward a binary search is used to find values in the array that match prime product sum of the anagram sentence given.

Lastly the possible word combinations are hashed and checked with given hash.

###Testing

The tests of the program can be run using pytest, when standing in the /tests folder.
Then running the command below in a terminal.

py.test --cov=test_word_prime_converter.py --cov=preproccessing --cov=fileIO --cov=md5_hashing
--cov=processing --cov=solver --cov=prime_number_generator --cov=utilities --cov-report=term --pep8 --flakes --mccabe

It is a bit clunky.

The tests cover 99% of the program.
The test coverage reports generated with pytest can be found in the /tests/htmlcov folder.
The html files can be opened in a browser.

There are still corner cases that are not tested yet though.

###Final remarks

The correct anagram sentence hash is found in about 0.34 sec on a i7-2700K.

Below are the run speeds of the process throughout optimization.
660 sec -> 5.7 sec -> 2.3 sec -> 0.5 sec -> 0.34 sec
