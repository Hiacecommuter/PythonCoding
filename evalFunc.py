#https://realpython.com/python-eval-function/
"""
expression vs statement
eval() only accept expression
eval(expression[, globals[, locals]])
"""

# eval() can assess global names
x =100
eval("x*2")

#use global
eval("x + 100", {"x": x})
eval("x + y + z", {"x": x, "y": y, "z": 300})

#use locals
eval("x + 100", {}, {"x": 100})

#Minimizing the secuirty issues of eval()
#Restricting globals and locals
x = 100
eval("x * 5", {}, {})
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined

 pass empty dictionaries to both arguments 
 to prevent eval() from accessing names in the caller’s current scope or namespace:
"""
