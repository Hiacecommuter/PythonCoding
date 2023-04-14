"""
calss coleections.deque([iterable[,maxlen]])
Returns a new deque object initialized left to right with data from iterable.
Deques support thread-safe, memory efficient appends and pops from either side of the deque with
approximately the same O(1) performance in either direction

Though list objects support similar operations, they are optimized for fast fixed-length operations 
and incur O(n) memory movement cost for pop(0) and insert(0,v) operations, which change both the size 
and position of the underlying data representation.

- append(x) add x to right
- appendleft(x)
- clear() remove all elements from deque leaving it with length 0
- count(x) count the number of deque elements equal to x
- extend(iterable) extend the right side of the deque by appending elements from the iterable argument
- extendleft(iterbale)
- pop()
- popleft()
- remove(value) remove he first occurance of value. If not found, raises a ValeError
- reverse() reverse the elements of the deque in-place and then return None
- rotate(n=1) n>0 to right, n< 0 to left
- maxlen Maximun size of deque or NOne if unbounded

https://docs.python.org/2/library/collections.html#collections.deque
"""
