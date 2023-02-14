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
"""
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
