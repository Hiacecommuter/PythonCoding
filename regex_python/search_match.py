"""
re.match matches must start from the text, otherwise returns None
re.search searches full text
"""
import re

re.search(Substring, String1, re.IGNORECASE)
re.match(Substring, String1, re.IGNORECASE)

# re.IGNORECASE is used to ignore the case sensitivity in the strings
