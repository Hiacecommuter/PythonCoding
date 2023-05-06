"""
yield is an expression, rather than a statement. You can still use it as a statement. 
But this allows you to manipulate the yielded value.
More importantly, it allows you to .send() a value back to the generator. 
When execution picks up after yield, i will take the value that is sent.
"""

"""send()
it sends 10 ** digits to the generator. 
This brings execution back into the generator logic and assigns 10 ** digits to i. 
Since i now has a value, the program updates num, increments, and checks for palindromes again
"""
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)     # coroutine
            if i is not None:
                num = i
        num += 1
        
pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))        
    
""" close()
.close() allows you to stop a generator.
"""
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
        # or pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
