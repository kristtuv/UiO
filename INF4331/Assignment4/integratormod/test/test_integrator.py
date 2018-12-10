import sys
sys.path.append("..") #Works in my python 2, but my anaconda pythonpath is broken for python 3
#sys.path.append("/Users/Tuv/Documents/UiO/UiOUpstream/INF3331-kristtuv/Assignment4/integratormod")

from integrator import integrate, midpoint_integrate
from numpy_integrator import numpy_integrate, numpy_midpoint_integrate
from numba_integrator import numba_integrate, numba_midpoint_integrate
from cython_integrator import cython_integrate, cython_integrate_sin, cython_midpoint_integrate_sin
from numpy import pi

def test_integral_of_constant_function():
	f = lambda x: 2
	a = 0.0; b = 1.0
	expected = 2.0

	N = 100
	computed = integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
	N = 1000
	computed = integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 100000
	computed = integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_integral_of_linear_function():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = integrate(f, a, b, N)
		assert abs(computed - expected) <= (1./N + 1e-12)

		N = 10000
		computed = integrate(f, a, b, N)
		assert abs(computed - expected) <= (1./N + 1e-12)
def test_integral_of_constant_function_numpy():
	f = lambda x: 2.0
	a = 0.0; b = 1.0;
	expected = 2.0

	N = 100
	computed = numpy_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
	N = 1000
	computed = numpy_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = numpy_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = numpy_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_integral_of_linear_function_numpy():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = numpy_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = numpy_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 10000
		computed = numpy_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)
def test_integral_of_constant_function_numba():
	f = lambda x: 2.0
	a = 0.0; b = 1.0;
	expected = 2.0

	N = 100
	computed = numba_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
	N = 1000
	computed = numba_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = numba_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = numba_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_integral_of_linear_function_numba():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = numba_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = numba_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 10000
		computed = numba_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

def test_midpoint_integral_of_constant_function():
	f = lambda x: 2
	a = 0.0; b = 1.0
	expected = 2.0

	N = 100
	computed = midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
	N = 1000
	computed = midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 100000
	computed = midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_midpoint_integral_of_linear_function():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) <= (1./N + 1e-12)

		N = 10000
		computed = midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) <= (1./N + 1e-12)
def test_midpoint_integral_of_constant_function_numpy():
	f = lambda x: 2.0
	a = 0.0; b = 1.0;
	expected = 2.0

	N = 100
	computed = numpy_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000
	computed = numpy_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = numpy_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = numpy_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_midpoint_integral_of_linear_function_numpy():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = numpy_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = numpy_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 10000
		computed = numpy_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)
def test_midpoint_integral_of_constant_function_numba():
	f = lambda x: 2.0
	a = 0.0; b = 1.0;
	expected = 2.0

	N = 100
	computed = numba_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
	N = 1000
	computed = numba_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 10000
	computed = numba_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10

	N = 1000000
	computed = numba_midpoint_integrate(f, a, b, N)
	assert abs(computed - expected) < 1e-10
def test_midpoint_integral_of_linear_function_numba():
		f = lambda x: 2*x
		a = 0.0; b = 1.0;
		expected = 1.0

		N = 100
		computed = numba_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 1000
		computed = numba_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

		N = 10000
		computed = numba_midpoint_integrate(f, a, b, N)
		assert abs(computed - expected) < (1./N + 1e-12)

def test_cython_midpoint_integrate_sin():
	a = 0.0; b = pi;
	expected = 2.0

	N = 1000000
	computed = cython_midpoint_integrate_sin(a, b, N)
	assert abs(computed - expected) < (1e-5)
def test_cython_integrate_sin():
	a = 0.0; b = pi;
	expected = 2.0

	N = 1000000
	computed = cython_integrate_sin(a, b, N)
	assert abs(computed - expected) < (1e-5)
def test_cython_integrate():
	a = 0.0; b = 1.0;
	expected = 1./3

	N = 1000000
	computed = cython_integrate(a, b, N)
	assert abs(computed - expected) < (1e-5)
