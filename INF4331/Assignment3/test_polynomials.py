from polynomials import Polynomial
def test_evaluate_at_points():
    p = Polynomial([1, 2, 3])
    exact1 = 6
    exact2 = 17
    exact3 = 34
    calc1 = p(1)
    calc2 = p(2)
    calc3 = p(3)
    msg = "Calculated 3x**2 + 2x + 1 at points 1, 2 and 3. Did not get same results as analytic result"
    assert (exact1 == calc1 and exact2 == calc2 and exact3 == calc3), msg

def test_add_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2])
    exact = "3x^2 + 4x + 2"
    addition = str(p1 + p2)
    assert exact == addition
def test_subtract_polynomials():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([1, 2])
    exact = "3x^2 "
    subtraction = str(p1-p2)
    assert exact == subtraction

def test_degree():
    p = Polynomial([1, 2, 3])
    q = Polynomial([3])
    r = Polynomial([0])
    pexact = 2
    qexact = 0
    rexact = -1
    assert (int(p.degree()) == pexact and int(q.degree()) == qexact\
            and int(r.degree()) == rexact)
def test_repr():
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([0, 2, 3])
    p3 = Polynomial([0, 3, 0])
    p4 = Polynomial([-1, 2, -2])
    p5 = Polynomial([-1, -2, -3])
    p6 = Polynomial([0, 0, 0])
    p1exact = "3x^2 + 2x + 1"
    p2exact = "3x^2 + 2x "
    p3exact = "3x "
    p4exact = "-2x^2 + 2x -1"
    p5exact = '-3x^2 -2x -1'
    p6exact = ""
    pstrings = [str(p1), str(p2), str(p3), str(p4), str(p5), str(p6)]

    pexactstrings = [p1exact, p2exact, p3exact, p4exact, p5exact, p6exact]
    for i, j in zip(pstrings, pexactstrings):
        assert i.split() == j.split()

def test_mul():
    c = 2
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([0, 4, 6])
    p1cexact = Polynomial([2, 4, 6])
    p2cexact = Polynomial([0, 8, 12])

    assert p1*c == c*p1 == p1cexact
    assert p2*c == c*p2 == p2cexact
