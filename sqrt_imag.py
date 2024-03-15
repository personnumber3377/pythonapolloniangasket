
# This file implements a square root of an imaginary number, because math.sqrt throws an error if you try to use it with imaginary numbers.

import math


'''


def sqrt_imag(num):
	# Big thanks to https://math.stackexchange.com/a/44414
	c = num.real
	d = num.imag
	#if d == 0.0: # The imaginary part is zero.
	#	return complex(math.sqrt(c), 0)

	a = math.sqrt((c + math.sqrt(c**2 + d**2)) / (2))
	if d == 0.0:

		b = 0 * (math.sqrt((-c + math.sqrt(c**2 + 0**2)) / 2))

	else:
		print("d == "+str(d))
		b = (d)/(abs(d)) * (math.sqrt((-c + math.sqrt(c**2 + d**2)) / 2))

	return complex(a,b) # Return this.

'''

def sqrt_imag(num):
	m = math.sqrt(num.real ** 2 + num.imag ** 2)
	print("m == "+str(m))
	angle = math.atan2(num.imag, num.real)
	print("angle == "+str(angle))
	m = math.sqrt(m)
	angle = angle / 2
	return complex(m * math.cos(angle), m * math.sin(angle))




def tests() -> int: # tests sqrt_imag

	test_num = complex(2,5)
	root = sqrt_imag(test_num)
	assert root**2 == test_num
	print("Tests passed!!!")
	return 0


if __name__=="__main__":
	exit(tests())

