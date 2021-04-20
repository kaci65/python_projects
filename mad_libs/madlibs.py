#!/usr/bin/python3
# mad libs generator (story template gotten from wikipedia)


# stoy variables
exclamation = input("Enter an exclamation word and hit enter: ")
word_adv = input("Enter an adverb and hit enter: ")
word_noun = input("Enter a noun and hit enter: ")
word_adj = input("Enter an adjective and hit enter: ")

# story
story = f"{exclamation}! he said {word_adv} as he jumped into his convertible {word_noun} and drove off with his {word_adj} wife."

print(story)

# # using str.format() instead of 'f-string'
# # stoy variables
# exclamation = input("Enter an exclamation word and hit enter: ")
# word_adv = input("Enter an adverb and hit enter: ")
# word_noun = input("Enter a noun and hit enter: ")
# word_adj = input("Enter an adjective and hit enter: ")

# # story
# story = "{}! he said {} as he jumped into his convertible {} and drove off with his {} wife."

# print(story.format(exclamation, word_adv, word_noun, word_adj))