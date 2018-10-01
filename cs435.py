import string
import operator

# Alphabet constant
alphabet = list(string.ascii_lowercase)

# Print the word from an array of numbers
def getWord (numberForm):
	word = ""
	for letter in numberForm:
		word += alphabet[letter % 26]
	return word

# Print the index of each string character
def getNumberForm (word):
	number_array = []
	for letter in word:
		number_array.append(
			alphabet.index(letter.lower())
		)
	return number_array

# Pass in a dictionary map of lowercase letter to lowercase letter
def printReplacedLetters(string, replacements):
	i = 1;
	for letter in string:
		endChar = "\n" if i % 40 == 0 else ""
		lower = letter.lower()
		print("\033[92m", end="")
		print(replacements.get(lower, "\033[0m" + lower), end=endChar);
		i += 1
	print("")
	return

# returns dictionary of letter counts
def getLettercounts(word):
	return dict((letter.lower(), word.lower().count(letter)) for letter in alphabet)

# find shift in order to produce the output char from the input char
def findShift(input, output):
	return alphabet.index(output.lower()) - alphabet.index(input.lower())

# shift strings
def shiftString(word, shift):
	numberForm = getNumberForm(word)
	numberForm[:] = [x + shift for x in numberForm]
	return getWord(numberForm)

# Calculte Index of Coincidence
def IC(lettercounts):
	total = 0;
	for letter, count in lettercounts.items():
		total += count * (count - 1)

	chars = sum(lettercounts.values())
	total = total / chars / (chars - 1)
	return total

# calculate average IC for a given number of columns
def kasiski (word, columns):
	average = 0;
	for n in range(columns):
		substring = word[n::columns]
		average += IC(getLettercounts(substring))
	average /= columns
	return average

# get array of strings when divided up for vigenere ciphertext
def divideString (word, columns):
	strings = []
	for n in range(columns):
		strings.append(word[n::columns])
	return strings

# recombine strings from vigenere ciphertext
def combineStrings (wordsArray):
	final = ""
	for i in range(len(wordsArray[0])):
		for word in wordsArray:
			if(i < len(word)):
				final += word[i]
	return final

# find all combinations of the characters of two strings
def findCombos (strings):
	num_of_possibilities = len(strings)**len(strings[0])

	num_of_duplicates = num_of_possibilities
	printedSoFar = 0

	possibilities = [''] * num_of_possibilities
	currentStringIndex = 0

	for currChar in range(len(strings[0])):
		printedSoFar = 0
		currentStringIndex = 0
		num_of_duplicates /= len(strings)
		for index in range(num_of_possibilities):
			if(printedSoFar == num_of_duplicates):
				printedSoFar = 0
				currentStringIndex = (currentStringIndex + 1) % len(strings)

			possibilities[index] += strings[currentStringIndex][currChar]
			printedSoFar += 1

	return possibilities

# computation for HW4
word = ("PPKVFAZUNGSSHUNKZLQYMUNMHFOWKIZYNAWHGSALU"
		"BHWKVVBOYTVJOHAPLJRLGIGYTLUGBYAUAPLCRZYCQULOULMAO"
		"CSANUVLWATSWHHCLFOVAQZMIKYAFLALLVLXVKJBVLYVPETSQC"
		"YRWIONHBZNATZOTKJYCDNYTJLMUCGTUTKJLPXILLDTVOIUWOI"
		"MKEMKNHLUTTPKZQIABTJYMHNIUUNGUKVONAYRVOIAQAZWOOWM"
		"ACTPPETHBOYRABAPJWTJESFIPNEVHTOYBCABSYOMNHGZBYCKL"
		"LSYPBOFICYRRVWSMFLLNCULVNOYLEUAWTUKLXEEPAPPEJINVY"
		"QIOTPINUHVKMEAOPEOMSMEHMWKU")

print(word)

# for i in range(1, 20):
# 	print(str(i) + ": " + str(kasiski(word, i)))
#
# print("---------------")

strings = divideString(word,9)
# print("Columns:")
# for string in strings:
# 	print(string)
#
# print("---------------")

combos = findCombos([
	"TSBVUILYO",
	"GAMLNTAUN",
	"KPAZYRZWA"])
# GLMLYELYE
# print(combos)
# print(len(combos))
for combo in combos:
	shiftedStrings = []
	for i in range(9):
		shift = findShift(combo[i], "E")
		shiftedStrings.append(shiftString(strings[i], shift).upper())
	combinedString = combineStrings(shiftedStrings)
	result = IC(getLettercounts(combinedString))
	print(combinedString[0:15])
	print("-----------------------------------")

# shiftedStrings = []
# decode = "NICOLASAN"
# for i in range(9):
# 	shift = findShift(word[i], decode[i])
# 	print(alphabet[(-shift) % 26], end="")
# 	shiftedStrings.append(shiftString(strings[i], shift).upper())
#
# print("-----------------------------------")
# print(combineStrings(shiftedStrings))
# print("-----------------------------------")

#Nicolas Anelka and Florent Malouda sent Chelsea back to the top of the Premier League as their second-half goals gave Carlo Ancelotti's side a deserved victory over Liverpool at Stamford Bridge.


# for i in range(9):
# 	s = strings[i]
# 	counts = getLettercounts(s)
# 	common = list(dict(sorted(counts.items(), key=operator.itemgetter(1), reverse=True)[:3]).keys())
#
# for combo in differentCombos:
# 	combineStrings(combo)
