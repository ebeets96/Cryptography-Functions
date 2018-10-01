
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
