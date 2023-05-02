"""
For class with many atttribute and method, it can be broken into smaller classes
""

class Battery():
  """A simple attempt to model a battery for an electric car."""
  def __init__(self, battery_size=70):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

  def describe_battery(self):
    """Print a statement describing the battery size."""
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""
  def __init__(self, make, model, year):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """
    super().__init__(make, model, year)
    self.battery = Battery()
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
