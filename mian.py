"""
Replace all the vowels in the string “National Center for Supercomputing Applications” by their corresponding order
number in alphabetical sequence (a with 1, e with 5, etc).

Print the resulting string.

Print the total number of consonants in the given string.
"""

word = 'National Center for Supercomputing Applications'
vowels = 'aeiou'

result = ''

for char in word:
    if char in vowels:
        # replace vowel characters their corresponding order number in alphabetical sequence
        result += str(ord(char) - ord('a') + 1)
    else:
        result += char

print(result)

consonants_counts = 0

for char in word:
    if char not in vowels:
        consonants_counts +=1

print('Total number of consonants in "' + word + '": ' + str(consonants_counts))
