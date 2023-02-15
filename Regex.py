import re

match = re.findall(Regex_Pattern, Test_String)

"""
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
"""
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
