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
w : 1
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






