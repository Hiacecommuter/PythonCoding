# Keep multiple whitespaces in a string when it is split

text = "hello   World   !"
# 1 use re
import re
result1 = re.split(r"(\s+)", text)
# for i in result1: ...

# 2 specify the delimiter in split()
result2 = text.split(" ")
result2 = " ".join(result2)

"""
If we specify space character argument in split function, 
it creates list without eating successive space characters. 
So, original numbers of space characters are restored after 'join' function.
'''
