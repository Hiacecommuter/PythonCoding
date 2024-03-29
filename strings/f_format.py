# basic use
name = "Jack"
age = 20
text = f"Hello, {name}. You are {age}."

# expression
f"{2 * 37}"
 f"{name.upper()} is funny."

class Comedian:
  def __init__(self, first_name, last_name, age):
      self.first_name = first_name
      self.last_name = last_name
      self.age = age

  def __str__(self):
      return f"{self.first_name} {self.last_name} is {self.age}."

  def __repr__(self):
      return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
    
new_comedian = Comedian("Jack", "Idle", "20")
f"{new_comedian}"    #str
f"{new_comedian!r}"   # repr
