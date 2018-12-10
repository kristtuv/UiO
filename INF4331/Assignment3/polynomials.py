class Polynomial:

	def __init__(self, coefficients):
		"""coefficients should be a list of numbers with
		the i-th element being the coefficient a_i."""
		if isinstance(coefficients, int):
			coefficients = [coefficients]
		if not isinstance(coefficients, (int, list)):
			raise ArithmeticError
		self.coefficients = coefficients

	def degree(self):
		"""Return the index of the highest nonzero coefficient.
		If there is no nonzero coefficient, return -1."""


		if all( x == 0 for x in self.coefficients):
			return -1
			exit(0)
		for i in range(len(self.coefficients)-1, -1, -1):
			if self.coefficients[i] == 0:
				continue
			else:
				return i
				break

	def coefficients(self):
		"""Return the list of coefficients.

		The i-th element of the list should be a_i, meaning that the last
		element of the list is the coefficient of the highest degree term."""
		return self.coefficients


	def __call__(self, x):
		"""Return the value of the polynomial evaluated at the number x"""
		value = 0
		for power, coeff in enumerate(self.coefficients):
			value += coeff*x**power
		return value

	def __add__(self, p):

		"""Return the polynomial which is the sum of p and this polynomial
		Should assume p is Polynomial([p]) if p is int.

		If p is not an int or Polynomial, should raise ArithmeticError."""


		while len(self.coefficients) < len(p.coefficients):
			self.coefficients.append(0)
		while len(self.coefficients) > len(p.coefficients):
			p.coefficients.append(0)
		_sum = []
		for i, j in zip(self.coefficients, p.coefficients):
			_sum.append(i+j)
		return Polynomial(_sum)

	def __sub__(self, p):

		"""Return the polynomial which is the difference of p
		 and this polynomial
		Should assume p is Polynomial([p]) if p is int.

		If p is not an int or Polynomial, should raise ArithmeticError."""

		while len(self.coefficients) < len(p.coefficients):
			self.coefficients.append(0)
		while len(self.coefficients) > len(p.coefficients):
			p.coefficients.append(0)
		_sub = []
		for i, j in zip(self.coefficients, p.coefficients):
			_sub.append(i-j)
		return Polynomial(_sub)

	def __mul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by given integer.
		Should raise ArithmeticError if c is not an int."""
		if not isinstance(c, int):
			raise ArithmeticError
		_mul = []
		for i in self.coefficients:
			_mul.append(i*c)
		return Polynomial(_mul)

	def __rmul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by given integer.
		Should raise ArithmeticError if c is not an int."""
		if not isinstance(c, int):
			raise ArithmeticError
		_rmul = []
		for i in self.coefficients:
			_rmul.append(c*i)
		return Polynomial(_rmul)

	def __repr__(self):
		"""Return a nice string representation of polynomial.

		E.g.: x^6 - 5x^3 + 2x^2 + x - 1
		"""
		first = True
		string = ""
		for power, coeff in reversed(list(enumerate(self.coefficients))):
			if coeff == 0: #Skip all zero coefficients
				continue

			elif coeff < 0: #So we can avoid +-sign when adding negative numbers

				if power == 1: #Avoid power-sign when power is one
					if coeff == -1:
						string += "-x "
					else:
						string += str(coeff) + "x "
				elif power == 0: #Avoid variable when power is zero
					string += str(coeff)
				else:
					if first: #If first value is negative, we do not want the
							#first positive value to skip adding the plus-sign
						string += str(coeff) + "x^" + str(power) + " "
						first = not first
					elif coeff == 1:
						string += "x^" + str(power) + " "
					else:
						string += str(coeff) + "x^" + str(power) + " "


			elif coeff > 0: #Add +-signes when we have positive numbers

				if power == 1: #Avoid power-sign when power is one

					if coeff == 1:
						if first:
							string += "x"
						else:
							string += "+ x "
					else:
						if first:
							string += str(coeff) + "x "
						else:
							string += "+ " + str(coeff) + "x "
				elif power == 0: #Avoid variable when power is zero
					if first:
						str(coeff)
						first = not first
					else:
						string += "+ " + str(coeff)
				else:
					if first: #Do not add +-sign in the first step
						if coeff == 1:
							string += "x^" + str(power) + " "
						else:
							string += str(coeff) + "x^" + str(power) + " "

						first = not first
					elif coeff == 1:
						string += "+ " + "x^" + str(power) + " "
					else:
						string += "+ " + str(coeff) + "x^" + str(power) + " "

		return string

	def __eq__(self, p):
		"""Check if two polynomials have the same coefficients."""
		while len(self.coefficients) < len(p.coefficients):
			self.coefficients.append(0)
		while len(self.coefficients) > len(p.coefficients):
			p.coefficients.append(0)
		flag = True
		for i, j in zip(self.coefficients, p.coefficients):
			if i == j:
				continue
			else:
				flag = False
				break

		return flag


def sample_usage():
	p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
	q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
	print("The value of {} at {} is {}".format(p, 7, p(7)))
	print("\nThe coefficients of {} are {}".format(p, p.coefficients))
	print("\nAdding {} and {} yields {}".format(p, q, p+q))

	p, q, r = map(Polynomial,[[1, 0, 1], [0, 2, 0], [1, 2, 1]])

	print("\nWill adding {} and {} be the same as {}? Answer: {}".format(p, q, r, p+q == r))
	print("\nIs {} - {} the same as {}? Answer: {}".format(p, q, r, p-q == r))
#sample_usage()
