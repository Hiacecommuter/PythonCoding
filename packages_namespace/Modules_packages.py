"""
Modular programming
    --  refers to the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules.

three different ways to define a module in Python:
  -- A module can be written in Python itself.
  -- A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
  -- A built-in module is intrinsically contained in the interpreter, like the itertools module.

Packages
    -- packages contains modules
    -- Packages allow for a hierarchical structuring of the module namespace using dot notation

Benefits for modularizing
  simplicity, maintainability, resusability, scoping
  """

"""The module Search Path
When interpreteer executes import statement, it searches for module_name.py in a list of directories assembled from
    -- The directory from which the input script was run or the current directory if the interpreter is being run interactively
    -- The list of directories contained in the PYTHONPATH environment variable, if it is set
    -- An installation-dependent list of directories configured at the time Python is installed
"""
import sys
sys.path # the resulting search path

"""
if module file is in arbitrary directory, can modity sys.path at run time
"""
sys.path.append(r'C:\Users\john')
sys.path

#check module location
mod.__file__

"""import
Each module has its own private symbol table, which serves as the global symbol table for all objects defined in the module.
Thus, a module creates a separate namespace
import only put module_name is the caller's symbol table
"""

"""from <module_name> import <name(s)> --Because this form of import places the object names directly into the caller’s symbol table, any objects that already exist with the same name will be overwritten
from <module_name> import * -- This will place the names of all objects from <module_name> into the local symbol table, with the exception of any that begin with the underscore (_) character.
from <module_name> import <name> as <alt_name> -- from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]
import <module_name> as <alt_name>
"""

dir()
"""
The built-in function dir() returns a list of defined names in a namespace. Without arguments, it produces an alphabetically sorted list of names in the current local symbol table
"""

import mod
dir(mod)  # lists the names defined in the module

"""
Modules are often designed with the capability to run as a standalone script for purposes of testing the functionality that is contained within the module. This is referred to as unit testing
"""
__name__
"""
Module initialization only executred when first time a module is imported
If you make a change to a module and need to reload it, you need to either restart the interpreter or use a function called reload() from module importlib:
"""
import mod      # __init__.py
import mod    # no initalization called, 
import importlib
importlib.reload(mod)

"""Packages
Packages allow for a hierarchical structuring of the module namespace using dot notation
Technically, a package is a Python module with an __path__ attribute
"""
"""
pkg contains mod1.py, mod2.py
"""
import pkg.mod1, pkg.mod2 # pkg directory has mod1.py and mod2.py
from pkg.mod1 import foo
import pkg  # import package

"""Package initialization
To create a Python package yourself, you create a directory and a file named __init__.py inside it.
The __init__.py file contains the contents of the package when it’s treated as a module. 
It can be left empty.
If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported.
"""
print(f'Invoking __init__.py for {__name__}')   # __init__.py
A = ['quux', 'corge', 'grault']     # __init__.py, Now when the package is imported, the global list A is initialized

"""
__init__.py can also be used to effect automatic importing of modules from a package.
__init__.py:
print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
then when you execute import pkg, modules mod1 and mod2 are imported automatically
"""
"""
 Python follows this convention: if the __init__.py file in the package directory contains a list named __all__, 
 it is taken to be a list of modules that should be imported when the statement from <package_name> import * is encountered
 pkg/__init__.py
__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]
"""

"""
_all__ can be defined in a module as well and serves the same purpose: to control what is imported with import *.
__all__ = ['foo']  # this is in the module py file

def foo():
    print('[mod1] foo()')

class Foo:
    pass 
"""   
"""
In summary, __all__ is used by both packages and modules to control what is imported when import * is specified. But the default behavior differs:

For a package, when __all__ is not defined, import * does not import anything.
For a module, when __all__ is not defined, import * imports everything (except—you guessed it—names starting with an underscore).
"""
"""subpackage
Or you can use a relative import, where .. refers to the package one level up
from ..sub_pkg1.mod1 import foo   # this pkg/sub__pkg2/mod3.py
"""
