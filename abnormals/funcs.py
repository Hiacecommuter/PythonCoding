# function default values is created at the first time of calling the function
# and it has been kept updating 

def append_to(element, to=[]):
    to.append(element)
    return to
my_list = append_to(12) #[12]
my_other_list = append_to(42) #[12, 42]


#https://docs.python-guide.org/writing/gotchas/
