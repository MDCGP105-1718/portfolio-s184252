from collections import defaultdict

# Hardcoded lyrics filenames
LYRICS1_FILENAME = "lyrics1.txt"
LYRICS2_FILENAME = "lyrics2.txt"

def create_freq_dict(usr_string):
	'''
	Creates a word frequency dictionary using the
	usr_string (string) input.
	'''

	usr_string_no_punc = []
	words_dict = defaultdict(int)

	# Converts usr_string to lowercase and strip out
	# all punctuation apart from apostrophes (').
	for c in usr_string.lower():
		if c in "abcdefghijklmnopqrstuvwxyz' \n":
			usr_string_no_punc.append(c)

	usr_string_no_punc = "".join(usr_string_no_punc)

	# Creates word frequency dictionary from all words
	# in usr_string.
	for word in usr_string_no_punc.split():
		words_dict[word] += 1

	return words_dict

def find_most_frequent_words(word_dict):
	'''
	Returns a tuple containing a list of the most frequently
	occuring word or words in the input frequency dictionary
	(dict{"word":frequency}), and the number of times the word(s) occur. 
	'''

	# Finds maximum frequency of all words.
	max_freq = max(word_dict.values())

	most_freq_words = []

	# Adds all words that occur with maximum frequency
	# to final word list.
	for key, value in word_dict.items():
		if value == max_freq:
			most_freq_words.append(key)

	return (most_freq_words, max_freq)

def find_words_frequency_at_least(word_dict, minimum_freq):
	'''
	Finds all words in the input frequency dictionary
	(dict{"word":frequency}) that occur at
	least as frequently as the minimum_freq (int).
	Returns a sorted list of tuples in ascending order of frequency,
	each containing a list of words found grouped by frequency,
	and the number of times the word(s) occur. 
	'''
	freq_dict = defaultdict(list)

	word_frequency_results = []

	for key, value in word_dict.items():
		if value >= minimum_freq:
			freq_dict[value].append(key)

	for key in sorted(freq_dict.keys()):
		word_frequency_results.append((freq_dict[key], key))

	return word_frequency_results

lyrics1 = open(LYRICS1_FILENAME, 'r').read()
most_freq_words = find_most_frequent_words(create_freq_dict(lyrics1))

print(f"Most Frequent - [{most_freq_words[1]} occurances]")
for n in most_freq_words[0]:
	print(n)

print()

lyrics2 = open(LYRICS2_FILENAME, 'r').read()
frequency_at_least_results = find_words_frequency_at_least(create_freq_dict(lyrics2), 3)

for tup in frequency_at_least_results:
	print(f"Frequency: [{tup[1]} occurances]")
	for word in tup[0]:
		print(word)