# Cryptography Functions
## Overview
These are some functions that I have been using for an intro to cryptography class.  You are free to use these in any way that you'd like, but know that I don't guarantee their correctness.

## `getWord(numberForm)`
This function accepts an array of integers and will convert that to a string where A is 0 mod 26, B is 1 mod 26, ..., and Z is 25 mod 26.

### Example
Input: `[0, 1, 2]`
Output: `"abc"`

## `getNumberForm(word)`
This is the inverse function of `getWord(numberForm)`.

### Example
Input: `"abc"`
Output: `[0, 1, 2]`

## `printReplacedLetters(string, replacements)`
This will replace the letters of a string with their cooresponding encryption/decription cipher, and will print the result using a green coloration on the characters that have been replaced.

### Example
Input:
	string: `abcdefg`
	replacements: `{"a":"z", "b": "y", "c":"x"}`

Output: "zyxdefg"

## `getLettercounts(word)`
This returns a dictionary containing key-value pairs of the English alphabet a..z and the corresponding number of occurrences in the string.

### Example
Input: `"aaabbcefhi"`

Output: `{'a': 3, 'b': 2, 'c': 1, 'd': 0, 'e': 1, 'f': 1, 'g': 0, 'h': 1, 'i': 1, 'j': 0, 'k': 0 ...}`
