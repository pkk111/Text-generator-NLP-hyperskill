# Write your code here
from nltk.tokenize import regexp_tokenize
from collections import defaultdict, Counter
import random
import re

file_name = input()
f = open(file_name, "r", encoding="utf-8")

tokens = []
for line in f:
    tokens.extend(regexp_tokenize(line, "[^\n \t]+"))

f.close()


def is_ender(word_to_check):
    return re.match(r'.*[.?!]$', word_to_check)  # word_to_check.endswith(".") or word_to_check.endswith('!') or word_to_check.endswith("?")


def is_starter(word_to_check):
    if len(word_to_check) < 2:
        return re.match(r'[A-Z]', word_to_check)
    return re.match(r'[A-Z].*[^.?!]$', word_to_check)


# creating bigrams
caps_tri = []
bigrams = []
j = 0
for i in range(len(tokens) - 2):
    if tokens[i] == '.' or tokens[i+1] == '.' or tokens[i+2] == '.':
        j += 1
        continue
    bigrams.append([])
    bigrams[i - j].append(tokens[i]+" "+tokens[i+1])
    bigrams[i - j].append(tokens[i + 2])
    if is_starter(tokens[i+1]):
        caps_tri.append(tokens[i] + " " + tokens[i+1])

bigram_dict = defaultdict(Counter)
for bigram in bigrams:
    bigram_dict[bigram[0]][bigram[1]] += 1

last_word = random.choice(bigrams)[0]
for _ in range(10):
    sent = ""
    i = 0
    just_ended = True
    new_line = True
    while i < 5 or not just_ended:
        next_possible_words = bigram_dict[last_word]
        words = []
        freqs = []
        for word, freq in next_possible_words.items():
            if not just_ended or is_starter(word.split()[0]):
                words.append(word)
                freqs.append(freq)
        if len(words) == 0:
            last_word = random.choice(bigrams)[0]
            continue
        else:
            next_word = random.choices(words, freqs)[0]
        if is_ender(next_word):
            just_ended = True
        else:
            just_ended = False
        if new_line:
            sent += next_word
            new_line = False
        else:
            sent += " " + next_word
        last_word = last_word.split()[1] + " " + next_word
        i += 1
    print(sent)
