
from circle import *
import math
from sqrt_imag import *
import math
import turtle

# This is the solution to the equation using three circles.

def descartes(c1, c2, c3) -> float: # This returns the bend of the fourth circle given three known circles which are all tangent to each other.
	k1 = c1.bend
	k2 = c2.bend
	k3 = c3.bend

	# Just calculate the answers using the formula.
	# k4 = -2 sqrt(k1 (k2 + k3) + k2 k3) + k1 + k2 + k3
	ans1 = -2*math.sqrt(k1*(k2 + k3) + k2*k3) + k1 + k2 + k3
	ans2 = 2*math.sqrt(k1*(k2 + k3) + k2*k3) + k1 + k2 + k3

	return [ans1, ans2]


def z4(c1, c2, c3, k4): # Returns the position of the circle thing (aka z4) (k4 must be first calculated with the descartes function)
	
	# You should pass both values of the bend of the last circle to this function
	assert isinstance(k4, list)
	assert len(k4) == 2

	k1 = c1.bend
	k2 = c2.bend
	k3 = c3.bend
	print("k1 == "+str(k1))
	print("k2 == "+str(k2))
	print("k3 == "+str(k3))
	# Convert centers of circles to complex numbers.

	z1 = complex(c1.x0, c1.y0)
	z2 = complex(c2.x0, c2.y0)
	z3 = complex(c3.x0, c3.y0)
	print("z1 == "+str(z1))
	print("z2 == "+str(z2))
	print("z3 == "+str(z3))
	root = k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3
	print("root == "+str(root))
	root_thing = 2 * sqrt_imag(k1*k2*z1*z2 + k2*k3*z2*z3 + k1*k3*z1*z3) # sqrt_imag is imported from sqrt_imag
	print("root_thing == "+str(root_thing))
	sum_shit = z1*k1 + z2*k2 + z3*k3
	print("sum == "+str(sum_shit))
	dividend1 = (z1*k1 + z2*k2 + z3*k3) + root_thing
	dividend2 = (z1*k1 + z2*k2 + z3*k3) - root_thing
	print("dividend1 == "+str(dividend1))
	print("dividend2 == "+str(dividend2))

	# Instead of returning the centers, let's just generate the circles here.
	#return [dividend1 / k4[0], dividend2 / k4[0], dividend1 / k4[1], dividend2 / k4[1]]

	centers = [dividend1 / k4[0], dividend2 / k4[0], dividend1 / k4[1], dividend2 / k4[1]]

	for i, cent in enumerate(centers):
		print("centers["+str(i)+"] == "+str(centers[i]))

	circ1 = Circle(centers[0].real, centers[0].imag, k4[0])
	circ2 = Circle(centers[1].real, centers[1].imag, k4[0])
	circ3 = Circle(centers[2].real, centers[2].imag, k4[1])
	circ4 = Circle(centers[3].real, centers[3].imag, k4[1])

	return [circ1, circ2, circ3, circ4]


SCALEFACTOR = 1

def render_circle(circle) -> None: # Shows one singular circle
	x_cent = circle.x0
	y_cent = circle.y0

	
	x_cent -= 400
	y_cent -= 400

	r = circle.radius
	turtle.penup()
	#turtle.goto(x_cent*SCALEFACTOR, y_cent*SCALEFACTOR)
	#turtle.dot(circle.radius*SCALEFACTOR) # Just draw a dot
	turtle.goto(x_cent*SCALEFACTOR, y_cent*SCALEFACTOR-r*SCALEFACTOR)
	#turtle.dot(100)
	turtle.pendown()
	turtle.circle(r*SCALEFACTOR)
	turtle.penup()

	return

EPSILON = 0.2

def validate(c4, c1, c2, c3, all_circles) -> bool: # Validates a circle thing.
	print("Checking shit!!!")
	if c4.radius < 2:
		print("Fuck!!")
		return False
	for other in all_circles:
		d = c4.get_center_to_center_distance(other)
		radiusDiff = abs(c4.radius - other.radius)
		if d < EPSILON and radiusDiff < EPSILON:
			print("Fuckkkkk!!!!")
			return False
	# Check tangents.
	if not c4.is_tangent_with(c1):
		return False
	if not c4.is_tangent_with(c2):
		return False
	if not c4.is_tangent_with(c3):
		return False
	print("Passed tests!!!!")
	return True

def main() -> int:
	# Try to calculate z4 for circles.
	# __init__(self, x0, y0, bend)
	turtle.tracer(0,0)
	turtle.speed(0)

	big_r = 400
	c1 = Circle(0+big_r, 0+big_r, -1 / (big_r)) # Circle at (0,0) with radius 2
	c2 = Circle((big_r/2)+big_r, 0+big_r, 1 / (big_r / 2)) # Circle at (1, 0) with radius 1
	c3 = Circle(-(big_r/2)+big_r, 0+big_r, 1 / (big_r / 2)) # Circle at (-1, 0) with radius 1

	# Now try to calculate the center of the fourth circle.

	# First calculate k4

	k4 = descartes(c1, c2, c3)
	print("k4 == "+str(k4))
	k4 = k4[1]

	#center_fourth = z4(c1, c2, c3, k4)
	#print(center_fourth[0])
	#center_fourth = center_fourth[0] # Get the first element
	#print("center_fourth == "+str(center_fourth))
	#x0 = center_fourth.real
	#y0 = center_fourth.imag
	# k4 is the curvature, therefore get the radius
	#radius = abs(1/k4)
	#print("radius == "+str(radius))


	all_circles = [c1,c2,c3] # List of all of the generated circles.
	queue = [[c1,c2,c3]] # This queue is all of the circle triplets I think
	#fourth_circle = Circle(x0, y0, k4)

	MAX_COUNT = 100000000
	counter = 0
	while True:

		# Here we probably want to add an infinite loop.

		if counter == MAX_COUNT:
			break


		counter += 1

		# First render all of the circles.

		for circ in all_circles:
			render_circle(circ)
		
		#input()
		# Now generate new circle triplets maybe??
		new_queue = [] # We will assign "queue" to this later on.
		for triplet in queue:
			c1,c2,c3 = triplet # Get the circles.
			k4 = descartes(c1, c2, c3)
			#print("k4 == "+str(k4))
			#k4 = k4[1]
			#radius_new = abs( 1 / k4 ) # Get the radius
			newCircles = z4(c1, c2, c3, k4)

			# Now generate new circles.
			# fourth_circle = Circle(x0, y0, k4)
			# Construct the new circles.
			#newCircles = [Circle(new_circle_centers[0].real, new_circle_centers[0].imag, k4[1]), Circle(new_circle_centers[1].real, new_circle_centers[1].imag, k4[1])]

			# Now append the new circles to the total circles list and then generate the new triplets.

			for new_circle in newCircles: # Loop through the generated circles.
				# Validate the circle shit.
				# validate(c4, c1, c2, c3, all_circles)
				if validate(new_circle, c1, c2, c3, all_circles):

					all_circles.append(new_circle)

					t1 = [c1, c2, new_circle]
					t2 = [c1, c3, new_circle]
					t3 = [c2, c3, new_circle]

					new_queue += [t1,t2,t3] # Append the triplets to the next queue.

		# Now the new queue is the queue for the next round

		queue = new_queue

		#render_circle(c1)
		#render_circle(c2)
		#render_circle(c3)
		#render_circle(fourth_circle)
		#turtle.goto(x0, y0)
		#turtle.dot(100)
		turtle.update()
		#turtle.clear()
	
	# Try to get input from stdin, such that we do not exit.
	input("Press enter to exit")

	return 0

if __name__=="__main__":
	exit(main())
