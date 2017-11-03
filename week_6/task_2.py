LYRICS1_FILENAME = "lyrics1.txt"
LYRICS2_FILENAME = "lyrics2.txt"

def find_most_frequent_words(lyrics):

	lyrics_no_punc = []
	words_dict = {}

	for c in lyrics.lower():
		if c in "abcdefghijklmnopqrstuvwxyz' \n":
			lyrics_no_punc.append(c)

	lyrics_no_punc = "".join(lyrics_no_punc)

	for word in lyrics_no_punc.split():
		if word not in words_dict:
			words_dict[words] = 1
		else:
			words_dict[word] += 1


lyrics1 = open(LYRICS1_FILENAME, 'r').read()

find_most_frequent_words(lyrics1)