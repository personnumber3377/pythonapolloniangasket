
import math
from typing import Type

# This file defines a circle class for convenience.

class Circle:
	def __init__(self, x0, y0, bend) -> None: # Constructor.
		self.x0 = x0
		self.y0 = y0
		self.center_pos = [x0, y0]
		self.radius = abs(1 / bend)
		self.bend = bend
	def get_center_to_center_distance(self, other_circle) -> float: # This returns the distance between the centers of this circle and other_circle.
		max_distance = self.radius + other_circle.radius # The maximum distance such that the circles do not overlap is r0 + r1
		distance_vector = [-self.x0+other_circle.x0, -self.y0+other_circle.y0] # Vector from this circle center to the other circle center.
		return math.sqrt(distance_vector[0]**2 + distance_vector[1]**2) # The actual distance using pythagoras.
	def overlaps_with(self, other_circle) -> bool: # This checks if this circle overlaps with other_circle .
		max_distance = self.radius + other_circle.radius
		actual_distance = self.get_center_to_center_distance(other_circle)
		return max_distance > actual_distance # Return true if overlaps, otherwise false
	def is_tangent_with(self, other_circle) -> bool: # Returns true if other_circle is tangent to this circle. Almost identical to the overlaps_with, but the comparison is equal to.
		max_distance = self.radius + other_circle.radius
		actual_distance = self.get_center_to_center_distance(other_circle)
		return max_distance == actual_distance # Return true if tangent. Otherwise false.

	def is_separate(self, other_circle) -> bool: # Returns true if other_circle is not tangent and also does not overlap with this circle.
		max_distance = self.radius + other_circle.radius
		actual_distance = self.get_center_to_center_distance(other_circle)
		return max_distance < actual_distance # Return true if doesn't overlap or isn't tangent. otherwise return false

def test_tangent() -> None:
	# Checks two circles which should be tangent to each other.
	c1 = Circle(0,0, - 1 / 200) # radius 200, therefore the center of the other circle should be at (400, 0) and the curvature or bend should be the same.
	c2 = Circle(400, 0, - 1 / 200)
	assert c1.is_tangent_with(c2)
	print("test_tangent passed!!!")

def test_is_separate() -> None:
	# Checks that two circles which should be separate, actually are separate according to the code.
	c1 = Circle(0,0, - 1 / 199)
	c2 = Circle(400, 0, - 1 / 199)
	assert c1.is_separate(c2) # They are slightly separated from each other
	print("test_is_separate passed!!!")



def tests() -> int: # Run tests
	test_tangent()
	test_is_separate()
	return 0

if __name__=="__main__": # If called as script, then run all tests.
	exit(tests())