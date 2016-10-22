# Anagram Solver
# The problem
I see the problem as two folded.

- Find words that is an anagram of "poultry outwits ants"
- The specific anagram must hash to 4624d200580677270a54ccff86b9610e

#Anagram definition
https://en.wikipedia.org/wiki/Anagram.
An anagram is made by rearranging the letters of a word or sentence such that a new word or phrase is created.



My initial thoughts.
Finding what words or word can create an anagram can be seen as a seperate problem.
If two sentences share exactly the same character they can make be a anagram.
The words combined must therefore have this number of characters:
a : 1
i : 1
o : 2
w : 12
t : 3
u : 2
l : 1
s : 2
n : 1
y : 1
p : 1
r : 1

Doing bruteforce on the problem would worst case be 18! which is 6.4023737e+15.


If the words are converted into an integer form i could leverage the numpy lib when finding potential
that could make anagrams.

Pros:

- Numpy does linear algebra computations very fast.
- With the integer convertion the order might not matter
  if added or multiplied together.
- It can be done in parallel on multiple cores of even GPU.

Cons:

- Preproccesing is needed, the amount of unique characters needs to be know.
- Adding more characters would require a new map to integers.



21/10/2016 19:00 thoughts:

Im unsure of what would be faster for eliminating invalid words.
The amount of words in the clean list is now 1787 after some preprocessing.

Trying to append the remaining words together combinatorially and checking the dictionary
of the anagram sentence if there are one too many of one character could be done.

Pros:

- It can avoid search on combinations has to many of one character.

Cons:

- It is alot of read and writes to dictionaries.


Another approach would be to multiply the prime products sums together and compare with
prime product sum of anagram sentence. This approach does not use the fact that a character
cant be repeated more times then in the anagram sentence.

Pros:

- The check for words combined that are larger is can be done fast
because if the product of the two words are larger then the anagram sentence sum
the combination is invalid.

Cons:

- Refined bruteforce.

Note:
The dublicates are being removed with the dictionary. Mabye this is a problem.


21/10/2016 22:30 thoughts:

It has become clear that im doing 6 times the amount of hashes for matching.
that is necessary, Ups.

Still thinking of a way to do computation with vector or matrix multiplications.
I speed would improve greatly because the computations can be off loaded to c-code with numpy.

#Ideas for optimization
22/10/2016 15:30 thoughts:
The part of the program that need optimizing is the processing section.
Currently its brute forcing to find solution.
In the search for product sum of the anagram sentence maybe a binary search could be used on the last loop.
because there wil only be one value multiplied that will give the sum.
Another idea would be to have a tree structure of the prime products combinations that would
sum to the wanted product.












