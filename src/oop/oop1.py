# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
  pass

# Class is subclass of Vehicle
class GroundVehicle(Vehicle):
  pass

# Class is subclass of Vehicle
class FlightVehicle(Vehicle):
  pass

# Classes are subclasses of GroundVehicle
class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass

# Classes are subclasses of FlightVehicle
class Airplane(FlightVehicle):
  pass

class Starship(FlightVehicle):
  pass