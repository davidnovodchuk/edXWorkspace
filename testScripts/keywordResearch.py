text = "one    two three  one"

wordsArray = text.split()

# 2D list that contains words and number of how many time the word apears
wordsApears = []

for i in wordsArray:
	
	# wordApears is one element in wordsApears
	wordApears = {}

	wordApears["word"] = i
	wordApears["apears"] = wordsArray.count(i)

	wordsApears.append(wordApears)

	wordsArray = [j for j in wordsArray if j != i]

wordsApears = [i for i in wordsApears if i['apears'] != 0]

wordsApears = sorted(wordsApears, key=lambda wordApears: wordApears['apears'], reverse=True)

for i in wordsApears:
	print i
	
