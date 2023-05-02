""" instance accesses to class attribute
"""
class ObjectCounter:
  num_instances = 0
  def __init__(self):
    ObjectCounter.num_instances += 1

""" __dict__
In a class, __dict__ contains class attributes and methods
In an instance, __dict__ contains instance attributes
""

"""Dynamic class and instance attributes
"""
# use setattr

class Record:
  """Hold a record of data."""
  
john = {
  "name": "John Doe",
  "position": "Python Developer",
  "department": "Engineering",
  "salary": 80000,
  "hire_date": "2020-01-01",
  "is_manager": False,
  }  
john_record = Record()

for field, value in john.items():
  setattr(john_record, field, value)
  
# direct approach
class User:
  pass
  
Amy = User()
Amy.name = "Amy"


