"""A set of classes that can be used to represent electric cars"""

from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size


    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car ha a {self.battery_size}-kWh battery.")


    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery() #if there is the class Battery
    # we add a specific attribute to subclass that is in comment because
    # the alternative is to make battery as a class
    #     self.battery_size = 75 


    # def describe_battery(self):
    #     """print a statement describing the battery size"""
    #     print(f"This car has a {self.battery_size}-kWh battery.")


    def fill_gas_tank(self):
        """electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")