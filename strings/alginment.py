# a string can be aligned left, right, and center.
width = 8
print("Hack".ljust(width, "-")) # Hack----
print("Hack".rjust(width, "-")) # ----Hack
print("Hack".center(width,"-")) # --Hack--


# swapcase
"HaCk".swapcase() # hAcK

# split and join
"-".join("this is a string".split())

# change one character in string

# str.capitalize()

# str.find() 
#This gives us the first index during a left to right scan. If the string is not found, it returns -1
print(testString1.find('llo'))
# Now, trying to find the index of a substring between specified indexes only
print(testString1.find('l',4,9))
#this scans the string from right to left
print(testString1.rfind('l'))

# str.replace()
print(testString1.replace("World","Planet"))

# Remove  whitespace
testString.strip() # leading and trailing
testString.rstrip() # from right, trailling

# split()
testString.split("delimiter", max_split)
testString.rsplit("delimiter", max_split)



