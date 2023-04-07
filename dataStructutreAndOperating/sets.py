#set is unorder, unchangeable, non duplicate,  can be mixed types
myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry", True, 1, 2}
len(thisset)

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) 

#index is same as list

#Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

#The object in the update() method does not have to be a set, 
#it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

#To remove an item in a set, use the remove(), or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

#pop can only remove a random element

thisset = {"apple", "banana", "cherry"}
thisset.clear() #clear elements
del thisset  # delete the variable

#methods
#union() intersection(), difference(), add(), symmetric_difference() both non common
