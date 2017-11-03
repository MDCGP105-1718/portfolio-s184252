# Hardcoded lyrics filenames
LYRICS1_FILENAME = "lyrics1.txt"
LYRICS2_FILENAME = "lyrics2.txt"

def find_most_frequent_words(usr_string):

	usr_string_no_punc = []
	words_dict = {}

	for c in usr_string.lower():
		if c in "abcdefghijklmnopqrstuvwxyz' \n":
			usr_string_no_punc.append(c)

	usr_string_no_punc = "".join(usr_string_no_punc)

	for word in usr_string_no_punc.split():
		if word not in words_dict:
			words_dict[word] = 1
		else:
			words_dict[word] += 1

	max_freq = max(words_dict.values())
	most_freq_words = []

	for key, value in words_dict.items():
		if value == max_freq:
			most_freq_words.append(key)

	return (most_freq_words, max_freq)


lyrics1 = open(LYRICS1_FILENAME, 'r').read()

print(find_most_frequent_words(lyrics1))