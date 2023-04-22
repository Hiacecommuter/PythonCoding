import re

match = re.findall(Regex_Pattern, Test_String)

"""
. any character \.

The expression \d matches any digit [ - ].
The expression \D matches any character that is not a digit.

\s matches any whitespace character [ \r\n\t\f ].
\S matches any non-white space character

\w will match any word character. Word characters include alphanumeric characters (-, - and -) and underscores (_).
\W matches any non-word character. Non-word characters include characters other than alphanumeric characters (-, - and -) and underscore (_).

The ^ symbol matches the position at the start of a string. 
The $ symbol matches the position at the end of a string.

The character class [ ] matches only one out of several characters placed inside the square brackets.
The negated character class [^] matches any character that is not in the square brackets.
A hyphen (-) inside a character class specifies a range of characters where the left and right operands are the respective lower and upper bounds of the range

The tool {x} will match exactly  repetitions of character/character class/groups \w{4} -> H_ck
  w{3} : It will match the character w exactly  times.
  [xyz]{5} : It will match the string of length  consisting of characters {x, y, z}. For example it will match xxxxx, xxxyy and xyxyz.
  \d{4} : It will match any digit exactly  times.
The {x,y} tool will match between  and  (both inclusive) repetitions of character/character class/group.
The * tool will match zero or more repetitions of character/character class/group.
  w* : It will match the character w  or more times.
  [xyz]* : It will match the characters x, y or z  or more times.
  \d* : It will match any digit  or more times.

The + tool will match one or more repetitions of character/character class/group.
   w+ : It will match the character w  or more times.
  [xyz]+ : It will match the character x, y or z  or more times.
  \d+ : It will match any digit  or more times.

The $ boundary matcher matches an occurrence of a character/character class/group
\b assert position at a word boundary.
Three different positions qualify for word boundaries :
    Before the first character in the string, if the first character is a word character.
    Between two characters in the string, where one is a word character and the other is not a word character.
    After the last character in the string, if the last character is a word character
() capture the group
(?:) not capture the group

|
  (Bob|Kevin|Stuart) will match either Bob or Kevin or Stuart.
  ([a-f]|[A-F]) will match any of the following characters: a, b, c, d, e, f, A, B, C, D, E, or F.
 
\number match the th group
  r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([A-Za-z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'
  
Backreference
    (b)?o\1  or (b?)o\1  \1only match is the referenced matached. 
    12-45-7810 later hyphen match depends on the first one, if the first one appears, the rest must match, vice versa. 

regex_1(?=regex_2)
The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. 
The lookahead is excluded from the match. It does not return matches of regex_2. 
The lookahead only asserts whether a match is possible or not

(?<=regex_2)regex_1
The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. 
Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.

regex_1(?!regex_2)
The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2. 
Lookahead is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
    Write a regex which can match all characters which are not immediately followed by that same character.
    r"(.)(?!\1)"

 (?<!regex_2)regex_1
The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. 
Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
"""
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())

"""
The findall() function returns a list containing all matches.
The list contains the matches in the order they are found.
If no matches are found, an empty list is returned

The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned
If no matches are found, the value None is returned

The split() function returns a list where the string has been split at each match
You can control the number of occurrences by specifying the maxsplit parameter

The sub() function replaces the matches with the text of your choice
You can control the number of replacements by specifying the count parameter

A Match Object is an object containing information about the search and the result.
If there is no match, the value None will be returned, instead of the Match Object.
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

"""
