
from choH import choH
import numpy
from pytest import approx

def test_size() :
    numpy.random.seed(0)
    X = [float(x) for x in list(numpy.random.normal(0,1,1000)) + list(numpy.random.normal(0.3,1,1000))]
    score = choH(X)
    assert len(score) == len(X) - 1

    
def test_min_val() :
    numpy.random.seed(0)
    X = [float(x) for x in list(numpy.random.normal(0,1,1000)) + list(numpy.random.normal(0.3,1,1000))]
    score = choH(X)
    assert min(score) == approx(-29.437,abs=1e-3)
