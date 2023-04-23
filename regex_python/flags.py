"""
re.I or re.IGNORECASE
    Perform case-insensitive matching; expressions like [A-Z] will also match lowercase letters.
    full unicode or re.ASCII (disable non-ascii matches)
re.A or re.ASCII

re.M or re.MULTILINE 
    When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline);
    the pattern character '$' matches at the end of the string and at the end of each line (immediately preceding each newline).
    By default, '^' matches only at the beginning of the string, and '$' only at the end of the string and immediately before the newline (if any) at the end of the string. Corresponds to the inline flag (?m).
    
re.NOFLAG

re.S or re.DOTALL
    Make the '.' special character match any character at all, including a newline; 
    
re.X or re.VERBOSE
    Allow comment and no meaning white space in the regex.
    
re.L or re.LOCALE

re.DEBUG
