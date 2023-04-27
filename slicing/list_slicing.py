#index
alist[::-1]  #reverse
alist[::2]  # index every second
alist[0:100]  #truncate if the number is greater than the maximum
alist[100:]

#insert
alist[len(alist):] = [9]    #insert at the end
alist[:0] = [1, 2]      #insert at the beginning
alist[3:3] = [1,2,3]    #insert at middle

#change
alist[:3] = [1,2,3]     #replace
alist[3:] = [ 1,2 3]    #replace
alist[::2] = [0]*3          # the number of elements should be equal
alist[::2]=['a', 'b', 'c'] # the number of elements should be equal

#del
alist[:3] = []
del alist[:3]
del alist[::2]
