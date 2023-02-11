"""
standard error has file desriptor 2
standard output has file descriptor 1
standard input has file descriptor 0
"""

"""
To pipe the output of Python program to a file
"""
# python myapp.py>output.txt

"""
To pipe standard error from the shell to a file while leaving standard outout going to the terminal
"""
#python myapp.py 2>errors.txt

"""
To pipe standard error in to stardard output
"""
#python myapp.py 2>&1

# Standard input defaults to keyboard in the terminal
print(type(sys.stdin))
letter = sys.stdin.read(1)  # Read 1 byte
print(letter)
# Can also do things like `sys.stdin.readlines()`

#sys.stdin.readlines() can be useful for reading a file that was piped in from the shell like this:
# Feed `input_file.txt` to `sys.stdin` of the Python script
#python my_script.py < input_file.txt

#To pipe the standard output of one program to the standard input of your Python program, you can do it like this:
#cat data.txt | python myapp.py

# Pipe file in via stdin
#python fileinput_example.py < file1.txt

# Provide list of files as arguments
#python fileinput_example.py file1.txt file2.txt file3.txt
